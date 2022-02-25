from cgi import test
from cgitb import text
import scrapy
import os
from datetime import datetime

from crypto_scraper.utils.array_utils import *
from crypto_scraper.utils.chain_utils import *
from crypto_scraper.utils.logger import sprint

from crypto_scraper.models.coin_model import *
from crypto_scraper.models.xpath_model import *
from crypto_scraper.models.chains_model import *

class CoingeckoSpider(scrapy.Spider):
    name = 'coingecko'
    start_urls = ['https://www.coingecko.com/en/coins/recently_added']
    custom_settings = {
        'FEED_URI': '../../../data/recently_added.json',
        'FEED_FORMAT': 'json',
        'ROBOTSTXT-OBEY': False,
        'FEED_EXPORT_ENCODING': 'utf-8'
    }

    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        sprint("Starting spider", self.name)

    def parse_coin(self, response, **kwargs):
        if kwargs:
            coin = Coin(
                name=kwargs['name'],
                id=kwargs['id'],
                href=kwargs['href']
            )
        
        coin.contract = response.xpath(xpath.coin.contract).get()
        coin.chain = format_chain(response.xpath(xpath.coin.chain).get())
        
        yield {
            coin.name: {
                "name": coin.name,
                "id": coin.id,
                "href": coin.href,
                "contract": coin.contract,
                "chain": coin.chain,
                "tracked_date": coin.tracking_date
            }
        }

    def parse(self, response, **kwargs):
        names = erase_line_jump(response.xpath(xpath.recently_added.coin_name).getall())
        IDs = erase_line_jump(response.xpath(xpath.recently_added.id).getall())
        hrefs = response.xpath(xpath.recently_added.coin_href).getall()
        last_added = erase_line_jump(response.xpath(xpath.recently_added.last_added).getall())

        for i in range(len(names)):
            if is_over_a_day(last_added[i]):
                yield response.follow(hrefs[i], callback=self.parse_coin, cb_kwargs={'name': names[i], 'id': IDs[i], 'href': hrefs[i]})
            
        #yield {
        #    "_comment": "This file will be overwrited every time coingecko is scraped.",
        #    "date": datetime.now(),
        #}       