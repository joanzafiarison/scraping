import scrapy 
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging

#full path 
from services.my_scrapper.scraper.spiders.entreprise import Entreprise

configure_logging({"LOG_FORMAT" : "%(levelname)s : %(message)s"})


def run_crawler():
    runner = CrawlerRunner()
    d = runner.crawl(Entreprise)
    d.addBoth(lambda _: reactor.stop())
    reactor.run() #script will block here until crawling is finished