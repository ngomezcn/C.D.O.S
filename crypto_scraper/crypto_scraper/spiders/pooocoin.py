import scrapy

class PoocoinSpider(scrapy.Spider):
    name = 'poocoin'
    start_urls = ['https://poocoin.app/tokens']
    custom_settings = {
        'FEED_URI': '../data/last_24h_new_tokens.json',
        'FEED_FORMAT': 'json',
        'ROBOTSTXT-OBEY': False,
        'FEED_EXPORT_ENCODING': 'utf-8'
    }
    
    def parse(self, response, **kwargs):
        
        pass