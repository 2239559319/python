# coding=utf-8
import sys
import requests
reload(sys)
sys.setdefaultencoding('utf-8')
headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
}
start=0000
while start<=3300:
    url='https://gaokao.chsi.com.cn/zzbm/mdgs/detail.action?oid=476754340&lx=1&start='
    url=url+str(start)
    print url[-4:]
    response=requests.get(url,headers=headers)
    response.encoding='utf-8'
    t=response.text
    print t
    if start==0:
        f=open(r'D:/a.txt','w+')
    else:
        f=open(r'D:/a.txt','a')
    f.write(t)
    start+=30
f.close()
if __name__=='__main__':
    main()