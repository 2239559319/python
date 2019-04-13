import scrapy
from ..items import ZhangyiItem

class zhangyiSpider(scrapy.Spider):

    name = "zhangyi"
    start_urls=["http://www.tcmap.com.cn/sichuan/leshan.html"]
    allowed_domains = ['tcmap.com.cn']

    def parse(self,response):
        msgs=[]
        tr=response.xpath("//table")[1].xpath("./tr[not(@align)]")       #每个区县的表格
        for t in tr:                                                         #每个区县里面的操作
            quxian=t.xpath("td[@align]/strong/a/text()").extract()             #区县名
            xiangzheng=t.xpath(".//div/a/text()").extract()                             #乡镇名
            xiangzhengUrl=t.xpath(".//div/a/@href").extract()
            for i in range(len(xiangzheng)):
                dic={}
                dic["name"]=xiangzheng[i]
                dic["url"]=xiangzhengUrl[i]
                msgs.append(dic)

        for msg in msgs:
            yield scrapy.Request("http://www.tcmap.com.cn/sichuan/"+msg["url"],meta={"name":msg["name"]},callback=self.getinfo)

    def getinfo(self,response):
        tr=response.xpath("//table").xpath("./tr[not(@align)]")
        shequlist=tr.xpath("td[@align]/strong/a/text()").extract()      #社区列表
        print(response.meta["name"],shequlist)

        item=ZhangyiItem(name=response.meta["name"],jiedao=" ".join(shequlist))
        yield item