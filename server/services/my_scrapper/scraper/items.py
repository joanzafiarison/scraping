# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
from itemloaders.processors import Join, MapCompose, TakeFirst
import re

import scrapy

def cleanString(str_):
    str_ = str_.replace("\n"," ")
    str_ = re.sub("\s+"," ",str_)
    return str_


class Proverb(scrapy.Item):
    # define the fields for your item here like:
    id = scrapy.Field(
        output_processor = Join()
    )
    proverb = scrapy.Field(
        input_processor = MapCompose(cleanString),
        output_processor = Join()
    )
    explanation_mg = scrapy.Field(
        input_processor = MapCompose(cleanString),
        output_processor = Join()
    )
    traduction = scrapy.Field(
        input_processor = MapCompose(cleanString),
        output_processor = Join()
    )
    explanation = scrapy.Field(
        input_processor = MapCompose(cleanString),
        output_processor = Join()
    )



class Simple(scrapy.Item):

    jauge =  scrapy.Field(
        output_processor = Join()
    )


class Mail(scrapy.Item):
    mail = scrapy.Field(
        output_processor = Join()
    )

    name = scrapy.Field(
        output_processor = Join()
    )

    phone = scrapy.Field(
        output_processor = Join()
    )
    

class EntrepriseItem(scrapy.Item):

    name =  scrapy.Field(
        output_processor = Join()
    )

    adress =  scrapy.Field(
        output_processor = Join()
    )

    postal =  scrapy.Field(
        output_processor = Join()
    )

    city =   scrapy.Field(
        output_processor = Join()
    )

    field = scrapy.Field(
        output_processor = Join()
    )

    code_APE =  scrapy.Field(
        output_processor = Join()
    )

class ScanItem(scrapy.Item):

    html =  scrapy.Field(
        output_processor = Join()
    )
    