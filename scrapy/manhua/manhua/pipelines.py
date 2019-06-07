# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request
import re
import os

class ManhuaPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        url_list=item["image_urls"].split(',')      #地址列表
        url='http://orhm.cn'
        for cur_url in url_list:
            yield Request(url=url+cur_url,meta={"manhuatitle":item["manhuatitle"],
                                                "huatitle":item["huatitle"],
                                                "name":cur_url.split('/')[-1]})

    def file_path(self, request, response=None, info=None):
        manhuatitle=request.meta["manhuatitle"].replace(' ','')
        huatitle=request.meta["huatitle"].replace(' ','')
        name = re.sub(r'[？\\*|“<>:/]', '', request.meta["name"])
        path='{0}/{1}/{2}'.format(manhuatitle,
                                  huatitle,
                                  name)
        return path

class FPipeline(object):

    def process_item(self, item, spider):
        if(not os.path.exists('E:\\Images\\'+item["manhuatitle"]+"\\desc.txt")):
            with open('E:\\Images\\'+item["manhuatitle"]+'\\desc.txt','w+') as f:
                f.write(item["desc"])

        return item