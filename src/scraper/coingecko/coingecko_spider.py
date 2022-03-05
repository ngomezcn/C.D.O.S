from cgi import test
from cgitb import text
import imp
import scrapy
import os
from std import dates_and_timestamps as std

from scraper.utils.array_utils import *
from scraper.utils.chain_utils import *
from scraper.utils.logger import sprint
from scraper.utils.time_format import time_since_added_to_date
from scraper.xpath import XpathCoingecko
from dbm.models import tables
from dbm.core import db
class CoingeckoSpider(scrapy.Spider):
    name = 'coingecko'
    
    start_urls = ['https://www.coingecko.com/en/coins/recently_added']
    custom_settings = {
        #'FEED_URI': '../out/spiders/coingecko/24h_new_tokens.json',
        #'FEED_FORMAT': 'json',
        'ROBOTSTXT-OBEY': False,
        'FEED_EXPORT_ENCODING': 'utf-8'
    }

    def parse_kwargs(self, kwargs):
        class parsed_kwargs():
            token_id = kwargs['token_id']
            token_name = kwargs['token_name']
            url_path = kwargs['url_path']
            listed_timestamp = kwargs['time_since_added']
            
        return parsed_kwargs()
    
    def get_contract(self, response, token_name):
        contract = response.xpath(XpathCoingecko.token.contract).get()
        if(contract == token_name): 
            return 'null'
        return contract
    
    def get_chain(self, response):
        return format_chain(response.xpath(XpathCoingecko.token.chain).get())
    
    def get_price(self, response):
        return float(response.xpath(XpathCoingecko.token.price).get()[1:].replace(',', ''))
    
    def get_listed_timestamp(self, response):
        # TODO: Finish that
        return std.get_timestamp() #- kwargs['time_since_added']
    
    def parse_raw_discovered_token(self, response, **kwargs):

        dt = tables.raw_discovered_token() 
        
        # Building token
        dt.token_id            = self.parse_kwargs(kwargs=kwargs).token_id
        dt.token_name          = self.parse_kwargs(kwargs=kwargs).token_name
        dt.url_path            = self.parse_kwargs(kwargs=kwargs).url_path
        dt.listed_timestamp    = self.get_listed_timestamp(response)
        dt.contract            = self.get_contract(response, dt.token_name)
        dt.chain_name          = self.get_chain(response)
        dt.ctp_id              = 'coingecko'
        dt.discovery_timestamp = std.get_timestamp()
        dt.price               = self.get_price(response)
        
        db.cinsert(dt) # Insert and commit new token to DataBase
        yield 

    def parse(self, response, **kwargs):
        token_names = erase_line_jump(response.xpath(XpathCoingecko.recently_added.coin_name).getall())
        token_ids = erase_line_jump(response.xpath(XpathCoingecko.recently_added.id).getall())
        url_paths = response.xpath(XpathCoingecko.recently_added.coin_href).getall()
        time_since_added = erase_line_jump(response.xpath(XpathCoingecko.recently_added.time_since_added).getall())
        time_since_added = time_since_added_to_date(time_since_added)

        for i in range(len(token_names)):
            yield response.follow(
                url_paths[i], 
                callback=self.parse_raw_discovered_token, 
                cb_kwargs= {
                            'token_id': token_ids[i], 
                            'token_name': token_names[i], 
                            'url_path': url_paths[i], 
                            'time_since_added': time_since_added[i]
                            })
    
    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        sprint("Starting spider", self.name)

    def __del__(self):
        sprint("Finish spider", self.name)