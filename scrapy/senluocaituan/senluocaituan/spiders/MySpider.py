from scrapy import Request
from scrapy import Spider
from ..items import SenluocaituanItem
import re

class SenluoSpider(Spider):

    name = 'senluo'

    def start_requests(self):
        for i in range(1, 28):
            yield Request(url='http://www.itmtu.com/ling/slct/page_{0}.html'.format(i),
                          callback=self.geteachurl)

    def geteachurl(self, response):
        urls = response.xpath('//ul[@id="index_ajax_list"]/li/a/@href').extract()

        for eachurl in urls:
            yield Request(url='http://www.itmtu.com' + eachurl,
                          meta={'image_urls': []},
                          callback=self.getpic)

    def getpic(self, response):

        cur_img_url = response.xpath('//div[@id="image_div"]/p/a/img/@src').extract_first()
        response.meta['image_urls'].append(cur_img_url)

        next_page = response.xpath('//div[@id="image_div"]//a[@title="下一页"]/@href').extract_first()
        if re.match(r'/mm/\d+/\d+', next_page) != None:
            yield Request(url='http://www.itmtu.com' + next_page,
                          meta=response.meta,
                          callback=self.getpic)
        else:
            item = SenluocaituanItem()
            item['image_urls'] = response.meta['image_urls']
            yield item

class MySpider(Spider):

    name = 'shaonvzhixu'

    def start_requests(self):
        for i in range(1, 4):
            yield Request(url='http://www.itmtu.com/ling/snzx/page_{0}.html'.format(i),
                          callback=self.geteachurl)

    def geteachurl(self, response):
        urls = response.xpath('//ul[@id="index_ajax_list"]/li/a/@href').extract()

        for eachurl in urls:
            yield Request(url='http://www.itmtu.com' + eachurl,
                          meta={'image_urls': []},
                          callback=self.getpic)

    def getpic(self, response):

        cur_img_url = response.xpath('//div[@id="image_div"]/p/a/img/@src').extract_first()
        response.meta['image_urls'].append(cur_img_url)

        next_page = response.xpath('//div[@id="image_div"]//a[@title="下一页"]/@href').extract_first()
        if re.match(r'/mm/\d+/\d+', next_page) != None:
            yield Request(url='http://www.itmtu.com' + next_page,
                          meta=response.meta,
                          callback=self.getpic)
        else:
            item = SenluocaituanItem()
            item['image_urls'] = response.meta['image_urls']
            yield item