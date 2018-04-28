#在程序中用两个不同的proxy设置
#encoding=utf-8

import urllib2
proxy=urllib2.ProxyHandler({'http':'127.0.0.1:8087'})
opener=urllib2.build_opener(proxy,)
response=opener.open("http://www.zhihu.com/")
print response.read()