#encoding=utf-8
#多媒体文件抽取
#urllib中的urlretrieve函数
#此程序只能在python2里面运行
import urllib
from lxml import etree
import requests
def schdule(blocknum,blocksize,totalsize):
    '''

    :param blocknum:已经下载的数据块
    :param blocksize: 数据块的大小
    :param totalsize: 远程文件的大小
    :return:
    '''
    per=100.0*blocknum*blocksize/totalsize
    if per>100:
        per=100
    print("当前下载进度:%d"%per)
r=requests.get('http://www.ivsky.com/tupian/ziranfengguang/')
html=etree.HTML(r.text)
img_urls=html.xpath('.//img/@src')#先找到所有的img
i=0
for img_url in img_urls:
    urllib.urlretrieve(img_url,'img'+str(i)+'.jpg',schdule)
    i+=1