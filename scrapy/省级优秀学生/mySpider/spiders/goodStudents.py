import scrapy
from scrapy.selector import XPathSelector
from scrapy.selector import Selector
from ..items import MyspiderItem

class goodStudentsSpider(scrapy.Spider):
    name = "goodStudents"
    start_urls=["https://gaokao.chsi.com.cn/zsgs/bsszgmd.do?method=listBySs&year=2018&jxId=31"]
    allowed_domains=['gaokao.chsi.com.cn']

    def parse(self, response):

        #实现抓取所有的链接然后进入
        urls=response.xpath("//div[@id='cnt1']//a//@href").extract()
        for url in urls:
            yield scrapy.Request("https://"+self.allowed_domains[0]+url,callback=self.getinfo)

    def getinfo(self,response):
        trs=Selector(response).xpath("//tr")
        for tr in trs:
            td=tr.xpath("./td/text()").extract()
            name=td[0]
            sex=td[1]
            province=td[2]
            school=td[3]
            item=MyspiderItem(name=name,sex=sex,province=province,school=school)
            yield item