from lxml import etree
import requests

url='https://www.baidu.com/'
r=requests.get(url=url)
r.encoding='utf-8'
#完善html代码
html=etree.HTML(r.text)
result=etree.tostring(html)
print(result)
#直接读取.html文件,用parse方法解析
html=etree.parse("index.html")
result=etree.tostring(html,pretty_print=True)
print(result)
#用XPath语法来抽取其中的URL
html=etree.HTML(r.text)
urls=html.xpath(".//*[@class='sister']/@href")
print(urls)