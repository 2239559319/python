import scrapy
import json
from ..items import ManhuaItem

class Manhua(scrapy.Spider):

    name = 'manhua'

    def start_requests(self):
        '''
        :return:
        '''
        url='http://orhm.cn/home/api/cate/tp/1-0-2-1-'
        for i in range(1,16):
            cur_url=url+str(i)
            yield scrapy.Request(url=cur_url,callback=self.get_list)

    def get_list(self,response):
        '''
        提取每个漫画的id,title，再发送进入目录请求
        :param response:
        :return:
        '''
        url='http://orhm.cn/home/api/chapter_list/tp/'
        msgs=json.loads(response.text)
        lists=msgs["result"]["list"]
        for list in lists:
            desc=list["desc"]           #漫画描述
            id=list["id"]
            manhuatitle=list["title"]
            cur_url=url+id+'-1-1-10'
            yield scrapy.Request(url=cur_url,callback=self.judge,   #判断是否目录不止一页
                                 meta={"id":id,
                                       "manhuatitle":manhuatitle,"desc":desc})

    def judge(self,response):
        '''
        判断漫画目录，发出每一话请求
        :param response:
        :return:
        '''
        url = 'http://orhm.cn/home/api/chapter_list/tp/'
        msgs=json.loads(response.text)
        total_row=msgs["result"]["totalRow"]        #总共的话数
        total_hua_page=int(int(total_row)/10)+1           #总共的页数
        for i in range(1,total_hua_page+1):
            cur_url=url+response.meta["id"]+'-1-'+str(i)+'-10'
            yield scrapy.Request(url=cur_url,callback=self.get_image,
                                 meta={"manhuatitle":response.meta["manhuatitle"],
                                       "desc":response.meta["desc"]})

    def get_image(self,response):
        '''
        获取每一话图片url
        :param response:
        :return:
        '''
        msgs=json.loads(response.text)
        huas=msgs["result"]["list"]     #每一话列表
        for i in huas:
            huatitle=i["title"]         #每一话标题
            urls=i["imagelist"]
            item = ManhuaItem(
                manhuatitle=response.meta["manhuatitle"],
                desc=response.meta["desc"],
                huatitle=huatitle,
                image_urls=urls)
            yield item