#用add_header来添加请求头信息
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
data=urllib.urlencode(postdata)
req=urllib2.Request(url)
#将user_agent,referer写入头信息
req.add_header('User-Agent',user_agent)
req.get_header('Referer',referer)
req.add_data(data)
response=urllib2.urlopen(req)
html=response.read()