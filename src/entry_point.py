#from dbm import CryptoTrackingPlatform, db

#new_ctp = CryptoTrackingPlatform('coingecko', 'coingecko.com', '104.148.544.127', 'https://www.coingecko.com/')
#db.cinsert(ne
# w_ctp)
#ctp = db.session.query(CryptoTrackingPlatform).get("coingecko")
#print(ctp.domain)

#from db.core.db_manager import db
#from db.models.discovery_system import *

#db.cinsert(CryptoTrackingPlatform('casd','asd','asdsad','asdsad'))

#print(db.session.query(ScrapedToken).count())
#from dbm.core.manager import db
#from dbm.models.discovery_system import crypto_tracking_platform, scraped_token 
#from dbm.models import tables


#db.cinsert(tables.crypto_tracking_platform('casd','asd','asdsad','asdsad'))

#print(db.session.query(ScrapedToken).count())

#from scraper.spiders.coingecko_spider import CoingeckoSpider
#import scrapy
#from twisted.internet import reactor
#from scrapy.crawler import CrawlerRunner
#from scrapy.utils.log import configure_logging
#from scrapy.utils.project import get_project_settings

#configure_logging()
#settings = get_project_settings()
#runner = CrawlerRunner(settings)
#runner.crawl(CoingeckoSpider, input)
#runner.crawl(AnotherSpider)
#d = runner.join()
#d.addBoth(lambda _: reactor.stop())

#reactor.run()