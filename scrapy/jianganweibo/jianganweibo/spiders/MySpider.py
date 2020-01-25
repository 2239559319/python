from scrapy import Request
from scrapy import Spider
from ..items import JianganweiboItem
import json
import time

class MySpider(Spider):

    name = 'weibo'

    def start_requests(self):
        baseurl = 'https://m.weibo.cn/api/container/getIndex?containerid=100101B2094757D06FA5F44093_-_weibofeed&luicode=10000011&lfid=231093_-_chaohua&page='
        for i in range(1, 10001):
            yield Request(url=baseurl + str(i), callback=self.parse)
            time.sleep(3)

    def parse(self, response):
        msg = json.loads(response.body, encoding='utf-8')
        weibo_lists = msg['data']['cards'][0]['card_group']

        for weibo in weibo_lists:
            msg = weibo['mblog']

            id = msg['id']
            created = msg['created_at']
            text = msg['text']
            name = msg['user']['screen_name']
            nameid = msg['user']['id']
            if('pics' in msg.keys()):
                pics = []
                for pic in msg['pics']:
                    pics.append(pic['url'])
            else:
                pics = None
            item = JianganweiboItem(name=name,
                                    nameid=nameid,
                                    id=id,
                                    created=created,
                                    text=text,
                                    pics=pics)
            yield item