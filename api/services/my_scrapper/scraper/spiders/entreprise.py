import scrapy
from scrapy.loader import ItemLoader
from services.my_scrapper.scraper.items import EntrepriseItem

class Sitemap():
    def __init__(self):
        pass 
    def getSitemap(self,name):
        #Find sitemap by id
        data = None
        if name == "verif.com":
            data = {
                "multi":"//div[contains(@class,'MuiBox-root') and contains(@class, 'css-1i3apa5') ]//tr",
                "single" :"//div[contains(@class,'MuiBox-root') and contains(@class, 'css-1wa5w4v')]",
                "link":"td/a/@href",
                "base_url":"https://www.verif.com",
                "name":"//h1[@class='MuiTypography-titleDesktopH1']/text()",
                "adress":"//td[contains(text(),'Adresse')]/following-sibling::div//span/text()",
                "code_APE":"//td[contains(text(),'NAF')]/following-sibling::div//span/text()",
                "site":"//span[contains(@class, 'MuiTypography-bodySmallMedium')  and contains(@class, 'css-1ymqwc8') ]/text()"
            }
        if name == "kompass":
            data = {
                "multi":"//div[@id='resultatDivId']//div[contains(@class,'prod_list')]",
                "single" :"//div[contains(@class,  'containerCompany')]",
                "name":"//h1[@itemprop='name']/span/text()",
                "adress":"//p[contains(@class,'blockAddress')]/span[contains(@class, 'spRight')]/text()",
                "postal":"",
                "city":"",
                "code_APE":"//table[contains(@class,'tableInfoJuridic')]/tbody/tr/th[contains(text(), 'Activités')]/following-sibling::td/text()",
                "site":"a[@id='webSite_presentation_0']/@href"
            }

        return data

class Entreprise(scrapy.Spider):
    name = "entreprise"

    start_urls = ["https://www.verif.com/Hit-parade/01-CA/01-Par-departement/67-Bas-Rhin/"]

    def __init__(self):
        self.site_id ="verif.com"
        st= Sitemap()
        self.sitemap = st.getSitemap(self.site_id)


    def start_request(self):
        for url in self.urls:
            yield scrapy.Request(url,callback=self.parse)


    def parse(self,response):
        il= ItemLoader(item=EntrepriseItem(),response=response)
        data = self.sitemap
        base_url = data["base_url"]
        #print("multi",response.xpath("//table[@id='verif_hitparade_donnees']").get())
        if response.xpath(data["multi"]).get() != None :
            #get links S
            #print(response.xpath("//table[@id='verif_hitparade_donnees']//tr"))
            items = response.xpath(data["multi"])
            #print("items",items)
            for element in items[2:]:
                #(element)
                #print("pasok")
                new_link =element.xpath(data["link"]).get()
                print("link ", new_link)
                yield scrapy.Request(url=base_url+""+new_link,callback=self.parse)

            
        else :
            #print("else")
            #print("single",response.xpath("//h1[@class='title']").get())
            
            name = response.xpath(data["name"]).get() #"//h1[@class='title']/text()"
            adress = response.xpath(data["adress"]).getall()
            city = response.xpath(data["city"]).getall()
            postal = response.xpath(data["postal"]).getall()
            code_APE = response.xpath(data["code_APE"]).get()
            #print("singlr",name)
            
            il.add_value("name",name)
            il.add_value("adress",adress)
            il.add_value("city",city)
            il.add_value("postal",postal)
            il.add_value("code_APE",code_APE)

            yield il.load_item()
            #request to the link and scrape