#获取http返回码
#encoding=utf-8

import urllib2
try:
    response=urllib2.urlopen('http://www.zhihu.com')
    print response
except urllib2.HTTPError as e:
    if hasattr(e,'code'):
        print 'Error code:',e.code