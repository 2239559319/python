#cookie自动处理
#encoding=utf-8

import urllib2
import cookielib
cookie=cookielib.CookieJar()
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response=opener.open('http://www.zhihu.com')
for item in cookie:
    print item.name+':'+item.value