from cgi import test
from cgitb import text
import imp
import scrapy
import os
import std

from scraper.utils.array_utils import *
from scraper.utils.chain_utils import *
from scraper.utils.logger import sprint
from scraper.utils.time_format import time_since_added_to_date

from scraper.models.coin_model import *
from scraper.models.chains_model import *
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

    def parse_raw_discovered_token(self, response, **kwargs):
        
        discovered_token = tables.raw_discovered_token()
        
        if kwargs:
            discovered_token.token_id = kwargs['token_id']
            discovered_token.token_name = kwargs['token_name']
            discovered_token.url_path = kwargs['url_path']
            discovered_token.listed_timestamp = std.get_timestamp() #- kwargs['time_since_added']
        
        discovered_token.contract = response.xpath(XpathCoingecko.token.contract).get()
        discovered_token.chain_name = format_chain(response.xpath(XpathCoingecko.token.chain).get())
        discovered_token.ctp_id = 'coingecko'
        discovered_token.discovery_timestamp = datetime.now().replace(microsecond=0)
        discovered_token.value = float(response.xpath(XpathCoingecko.token.price).get()[1:].replace(',', ''))
        
        if(discovered_token.contract == discovered_token.token_name.lower()): 
            discovered_token.contract = 'null'
        
        db.cinsert(discovered_token)
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