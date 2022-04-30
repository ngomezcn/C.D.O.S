from scraper.coingecko.coingecko_spider import CoingeckoSpider
import scrapy
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings

configure_logging()

settings = get_project_settings()
runner = CrawlerRunner(settings)
runner.crawl(CoingeckoSpider, input)

runner.join().addBoth(lambda _: reactor.stop())
reactor.run()
