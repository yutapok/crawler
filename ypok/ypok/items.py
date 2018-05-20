# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YpokItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    DOMAIN = scrapy.Field()
    LAST_BUILD = scrapy.Field()
    FLAG = scrapy.Field()
    TITLE = scrapy.Field()
    LINK = scrapy.Field()
    PUBDATE = scrapy.Field()
    LATEST = scrapy.Field()
