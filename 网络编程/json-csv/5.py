#encoding=utf-8
from lxml import etree
import requests
import re
import csv

url='http://seputu.com/'
r=requests.get(url=url)

html=etree.HTML(r.text)
div_mulus=html.xpath('.//*[@class="mulu"]') #先找到所有的div class =mulu标记
for div_mulu in div_mulus:
    #找到所有的div_h2标记
    div_h2=div_mulu.xpath('./div[@class="mulu-title"]/center/h2/text()')
    if len(div_h2)>0:
        h2_title=div_h2[0].encode('utf-8')
        a_s=div_mulu.xpath('./div[@class="box"]/ul/li/a')
        for a in a_s:
            href=a.xpath('./@href')[0]
            box_title=a.xpath('./@title')[0].encode('utf-8')

pattern=re.compile(r'\s*\[(.*)\]\s+(.*)')
match=pattern.search(box_title)
if match!=None:
    data=match.group(1)
    real_title=match.group(2)

html=etree.HTML(r.text)
div_mulus=html.xpath('.//*[@class="mulu"]')
pattern=re.match(r'\s*\[(.*)\]\s+(.*)')
rows=[]
for div_mulu in div_mulus:
    #找到所有的div_h2标记
    div_h2=div_mulu.xpath('./div[@class="mulu-title"]/center/h2/text()')
    if len(div_h2)>0:
        h2_title=div_h2[0].encode('utf-8')
        a_s=div_mulu.xpath('./div[@class="box"]/ul/li/a')
        for a in a_s:
            href=a.xpath('./@href')[0].encode('utf-8')
            box_title=a.xpath('./@title')[0].encode('utf-8')
            pattern = re.compile(r'\s*\[(.*)\]\s+(.*)')
            match = pattern.search(box_title)
            if match != None:
                data = match.group(1).encode('utf-8')
                real_title = match.group(2).encode('utf-8')
                content=(h2_title,real_title,href,data)
                print(content)
                rows.append(content)
headers=['title','real_title','href','data']
with open('D:/txt/qi.csv','w') as f:
    f_csv=csv.writer(f,)
    f_csv.writerow(headers)
    f_csv.writerows(rows)