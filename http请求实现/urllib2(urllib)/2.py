#get方法
#encoding=utf-8
import urllib2
#请求
request=urllib2.Request('http://www.zhihu.com')
#响应
response=urllib2.urlopen(request)
html=response.read()
print html