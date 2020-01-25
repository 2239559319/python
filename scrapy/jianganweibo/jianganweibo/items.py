# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JianganweiboItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()           #微博账号名
    nameid = scrapy.Field()         #微博账号id

    id = scrapy.Field()             #此条微博id
    created = scrapy.Field()        #发布时间
    text = scrapy.Field()           #微博内容
    pics = scrapy.Field()           #微博图片地址