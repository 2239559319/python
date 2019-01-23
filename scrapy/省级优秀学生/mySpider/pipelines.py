# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MyspiderPipeline(object):
    def __init__(self):
        self.file=open("a.txt",'w',encoding="utf-8")
    def process_item(self, item, spider):
        self.file.write(item["name"])
        self.file.write("    ")
        self.file.write(item["sex"])
        self.file.write("    ")
        self.file.write(item["province"])
        self.file.write("    ")
        self.file.write(item["school"])
        self.file.write("\n")
        return item
