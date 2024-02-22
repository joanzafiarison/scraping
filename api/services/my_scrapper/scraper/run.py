import scrapy 
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
import pathlib

#full path 
from services.my_scrapper.scraper.spiders.entreprise import Entreprise
from services.my_scrapper.scraper.spiders.scan import Scan

configure_logging({"LOG_FORMAT" : "%(levelname)s : %(message)s"})


def run_crawler(config):

    #1 - Configure Crawler --> Scrapy ou pas , config etc
    #le crawler doit être async

    #1b - Scrapy
    s = get_project_settings()
    s["FEEDS"] = {
            pathlib.Path('items.json') : {
                'format': 'json',
                'encoding': 'utf8',
                'store_empty': False,
                'overwrite':True,
                'indent': 4
            }
    }

    runner = CrawlerRunner(settings=s)

    #2 - Spécifier le sitemap / ou pas si automatique 

    #3 - décollage

   
    d = runner.crawl(Scan, data_source = config["data"])
    d.addBoth(lambda _: reactor.stop())
    reactor.run() #script will block here until crawling is finished