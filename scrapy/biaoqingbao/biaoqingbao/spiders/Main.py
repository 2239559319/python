from ..items import BiaoqingbaoItem
import scrapy

class MySpider(scrapy.Spider):

    name = 'biaoqingbao'
    allowed_domains=['fabiaoqing.com']

    def start_requests(self):
        url='https://fabiaoqing.com/biaoqing/lists/page/'
        for i in range(1,201):
            yield scrapy.Request(url+str(i)+'.html',callback=self.parse)

    def parse(self, response):
        image_urls=response.xpath('//img[@data-original]/@data-original').extract()
        item = BiaoqingbaoItem()
        item['image_urls']=image_urls
        yield item