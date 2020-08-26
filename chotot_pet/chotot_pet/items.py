# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Compose, TakeFirst

to = Compose(TakeFirst())

class Pet(Item):
    id = Field()
    url = Field()
    title = Field()
    price = Field()
    tel = Field()
    district = Field()
    seller = Field()
    seller_type = Field()
    crawled_time = Field()
    posted_time = Field()

class MyItemLoader(ItemLoader):
    default_item_class = Pet
    id_out = to
    url_out = to
    title_out = to
    price_out = to
    tel_out = to
    district_out = to
    seller_out = to
    seller_type_out = to
    crawled_time_out = to
    posted_time_out = to
