from sqlite3 import Date
from tokenize import String
import scrapy
from crypto.utils.strings import *
from crypto.models.coin import *
from crypto.xpath.coingecko import *
import sys

class CoingeckoSpider(scrapy.Spider):
    name = 'coingecko'
    start_urls = ['https://www.coingecko.com/en/coins/recently_added']
    custom_settings = {
        'FEED_URI': 'data/tokens.json',
        'FEED_FORMAT': 'json',
        'ROBOTSTXT-OBEY': False,
        'FEED_EXPORT_ENCODING': 'utf-8'
    }
    
    def parse_coin(self, response, **kwargs):
        if kwargs:
            coin = Coin(
                name=kwargs['name'],
                id=kwargs['id'],
                href=kwargs['href']
            )
        yield {
                coin.name: {
                    "id": coin.id,
                    "href": coin.href
                }
        }
    
    def parse(self, response, **kwargs):
        names = erase_line_jump(response.xpath(xpath.recently_added.coin_name).getall())
        IDs = erase_line_jump(response.xpath(xpath.recently_added.id).getall())
        hrefs = response.xpath(xpath.recently_added.coin_href).getall()

        for i in range(len(names)):
            yield response.follow(hrefs[i], callback=self.parse_coin, cb_kwargs={'name':names[i], 'id': IDs[i], 'href': hrefs[i]})
        
        