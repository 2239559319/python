# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ManhuaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    manhuatitle=scrapy.Field()     #漫画名
    desc=scrapy.Field()             #漫画描述
    huatitle=scrapy.Field()         #话名(第几话)
    image_urls=scrapy.Field()       #图片地址