import scrapy
from ..items import Pro1Item

class scuspider(scrapy.Spider):
    name = "scu"
    start_urls=["http://www.scu.edu.cn/"]
    def parse(self, response):
        news=response.xpath("//*[@class='news-list']//a")
        for new in news:
            text=new.xpath("./text()").extract()[0]
            item=Pro1Item(text=text)
            yield item