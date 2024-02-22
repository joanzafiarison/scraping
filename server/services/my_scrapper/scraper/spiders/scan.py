from typing import Iterable
import scrapy
from scrapy.loader import ItemLoader
from scrapy.http import Request
from services.my_scrapper.scraper.items import ScanItem



class Scan(scrapy.Spider):
    name = "scan"
    #start_urls = ['https://www.verif.com/societe/HOLDING-SOPREMA-558500187/']

    def __init__(self, data_source):
        self.data_source = data_source
        self.urls = data_source["urls"]
        self.model = data_source["model"]
    
    def start_requests(self) -> Iterable[Request]:
        print("start request")
        for url in self.urls:
            yield scrapy.Request(url,callback=self.parse)

    def parse(self,response):
        il= ItemLoader(item=ScanItem(),response=response)
        print("resp ",response.text)
        #pour chaque clé du model trouver un candidat
        #Postal Code 
        #Adresse
        #NAF
        il.add_value("html",response.text)
        yield il.load_item()

