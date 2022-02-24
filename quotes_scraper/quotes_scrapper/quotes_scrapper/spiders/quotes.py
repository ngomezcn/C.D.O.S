from gc import callbacks
import scrapy

# Titulo = //h1/a/text()
# Citas = //span[@class="text" and @itemprop="text"]/text()
# Top ten = //div[contains(@class, 'tags-box')]//a[contains(@class, 'tag')]/text()
# Next page button = //ul[@class="pager"]//li[@class="next"]/a/@href
# 

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com'
    ]
    custom_settings = {
        'FEED_URI': 'quotes.json',
        'FEED_FORMAT': 'json',
        'CONCURRENT_REQUESTS': 24,
        'MEMUSAGE_LIMIT_MB': 2048,
        'MEMUSAGE_NOTIFY_MAIL': ['naimgomezcn@gmail.com'],
        'ROBOTSTXT-OBEY': True,
        'USER_AGENT': 'ngomezcn',
        'FEED_EXPORT_ENCODING': 'utf-8'
    }

    def parse_only_quotes(self, response, **kwargs):
        if kwargs:
            quotes = kwargs['quotes']
            authors = kwargs['authors']
        quotes.extend(response.xpath('//span[@class="text" and @itemprop="text"]/text()').getall())
        authors.extend(response.xpath('//small[@class="author"]/text()').getall())

        
        next_page_button_link = response.xpath('//ul[@class="pager"]//li[@class="next"]/a/@href').get()
        if next_page_button_link:
            yield response.follow(next_page_button_link, callback=self.parse_only_quotes, cb_kwargs={'quotes': quotes, 'authors': authors})
        else:
            quotes_author =[]
            quotes_author = list(zip(quotes, authors))
            yield {
                'quotes': quotes_author
            }
    
    def parse(self, response):
        title = response.xpath('//h1/a/text()').get()
        quotes = response.xpath('//span[@class="text" and @itemprop="text"]/text()').getall()
        authors = response.xpath('//small[@class="author"]/text()').getall()
        
        top_tags = response.xpath(
            '//div[contains(@class, "tags-box")]//a[contains(@class, "tag")]/text()').getall()

        top = getattr(self, 'top', None)
        if top: 
            top = int(top)
            top_tags = top_tags[:top]

        yield {
            'title': title,
            'top_tags': top_tags
        }

        next_page_button_link = response.xpath('//ul[@class="pager"]//li[@class="next"]/a/@href').get()
        if next_page_button_link:
            yield response.follow(next_page_button_link, callback=self.parse_only_quotes, cb_kwargs={'quotes': quotes, 'authors': authors})
            
    