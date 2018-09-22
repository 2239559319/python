
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json


class Pro1Pipeline(object):
    def __init__(self):
        self.file=open("news.json","w",encoding="utf-8")
    def process_item(self, item, spider):
        if(item["text"]):
            line=json.dumps(dict(item),ensure_ascii=False)+"\n"
            self.file.write(line)
        return item
