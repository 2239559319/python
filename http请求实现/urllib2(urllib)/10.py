#检测是否发生了重定向动作
#encoding=utf-8

import urllib2
response=urllib2.urlopen('http://www.zhihu.cn')
isRedirected=response.geturl()=='http://www.zhihu.cn'