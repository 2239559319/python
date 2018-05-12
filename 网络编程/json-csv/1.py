#encoding=utf-8
from bs4 import BeautifulSoup
import requests
import json
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
}
url='http://seputu.com/'
r=requests.get(url=url,headers=headers)
content=[]

soup=BeautifulSoup(r.text,'html.parser',from_encoding='utf-8')#html.parser
for mulu in soup.find_all(class_="mulu"):
    h2=mulu.find('h2')
    if h2!=None:
        h2_title=h2.string #获取标题
        list=[]
        for a in mulu.find(class_='box').find_all('a'): #获取所有的a标记中的url和章节内容
            href=a.get('href')
            box_title=a.get('title')
            list.append({'href':href,'box_title':box_title})
        content.append({'title':h2_title,'content':list})
with open('D:/txt/qiye.json','w') as fp:
    json.dump(content,fp=fp,indent=4)