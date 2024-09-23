# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderbollItem(scrapy.Item):
    # define the fields for your item here like:
    code = scrapy.Field()
    red = scrapy.Field()
    blue = scrapy.Field()
    pass
