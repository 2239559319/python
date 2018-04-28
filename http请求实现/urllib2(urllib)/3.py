#encoding=utf-8
#post方法
import urllib
import urllib2
url='http://www.xxxxxx.com/login'
postdata={
    'username':'qiye',
    'password':'qiye_pass'
}
#info需要被编码为urllib2能理解的格式，这里用到的是urllib
data=urllib.urlencode(postdata)
req=urllib2.Request(url,data)
response=urllib2.urlopen(req)
html=response.read()