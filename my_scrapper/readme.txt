scrapy startproject my_scrapper C:\Users\elian\AppData\Roaming\Python\Python311\site-packages\scrapy\templates\project

scrapy crawl dico_mada -o result.csv




TYPE D'extracteur 

PAttern : ABB ABB 
Clasique (avec id)

Scanner : IA TEXT




Process : 

run one 
test all sitemaps 


Error : -- Error (Xpath/timeout/404)


TEST

pytest my_scrapper/tests/selector.py



XPATH 

response.xpath("//h1[@class='title']").get() => recup l'élement
 response.xpath("//h1[@class='title']/text()").get() => recup le text

response.xpath("//td[contains(text(),'Adresse')]/following-sibling::td//span[@itemprop='postalCode']/text()").getall()=> avec following sibling