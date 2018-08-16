# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ExpocrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

#Item class to soter the image filed and image url
class ExponeaImages(scrapy.Item):
    image_urls = scrapy.Field()
    images = scrapy.Field()