#动态设置代理
#encoding=utf-8

import urllib2
proxy=urllib2.ProxyHandler({'http':'127.0.0.1:8087'})
opener=urllib2.build_opener([proxy,])
urllib2.install_opener(opener)
response=urllib2.urlopen('http://www.zhihu.com')
print response.read()