#请求头header处理
#encoding=utf-8

import urllib
import urllib2
url='http://www.xxxxx.com/login'
user_agent='Mozilla/4.0 (compatible;MSIE 5.5; Windows NT)'
referer='http://www.xxxxx.com/'
postdata={
    'username': 'qiye',
    'password': 'qiye_pass'
}
#将user_agent,referer写入头信息
headers={'User-Agent':user_agent,'Referer':referer}
data=urllib.urlencode(postdata)
req=urllib2.Request(url,data,headers)
response=urllib2.urlopen(req)
html=response.read()