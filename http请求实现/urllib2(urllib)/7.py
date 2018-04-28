#自己添加cookie内容
#encoding=utf-8

import urllib2
opener=urllib2.build_opener()
opener.addheaders.append(('Cookie','email='+"xxxxxxx@163.com"))
req=urllib2.Request("http://www.zhihu.com")
response=opener.open(req)
print response.headers
retdata=response.read()