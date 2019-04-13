# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class ZhangyiPipeline(object):
    def __init__(self):
        self.file=open("a.json","w+",encoding="utf-8")


    def process_item(self, item, spider):
        dic={}
        dic[item["name"]]=item["jiedao"]
        line=json.dumps(dic,ensure_ascii=False)+"\n"
        self.file.write(line)
        return item