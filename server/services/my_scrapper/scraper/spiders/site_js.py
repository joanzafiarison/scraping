import scrapy 

from scrapy.loader import ItemLoader
from my_scrapper.items import Simple


class CNN(scrapy.Spider):

    #splash
    name="CNN"
    start_urls= ["https://edition.cnn.com/markets/fear-and-greed"]

    def start_request(self):
        for url in self.urls:
            yield scrapy.Request(url,callback=self.parse)


    def parse(self,response):
        il = ItemLoader(item=Simple(),response=response)
        jauge = response.xpath("//h1[@id='maincontent']").get()  #//span[@class='market-fng-gauge__dial-number-value']").get()
        print(response)
        il.add_value("jauge",jauge)
        il.load_item()
