import scrapy
from scrapy.loader import ItemLoader
from my_scrapper.items import Mail

class Florida(scrapy.Spider):

    name="florida"

    start_urls=['https://www.floridabar.org/directories/find-mbr/?locType=T&locValue=Pinellas&sdx=N&eligible=N&deceased=N&pageNumber=1&pageSize=10']


    def start_request(self):
        for url in self.urls:
            yield scrapy.Request(url,callback=self.parse)

    def parse(self,response):
        
        for item in response.xpath("//div[class='profile-contact']/p[2]"):
            il = ItemLoader(item=Mail(),response=response)
            mail = item.xpath("text()").get()
            il.add_value("mail",mail)
            #il.add_value("mail",mail)
            yield il.load_item()