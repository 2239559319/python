#encoding=utf-8
import requests
from bs4 import BeautifulSoup

url='https://www.baidu.com/?tn=sitehao123_15'
r=requests.get(url)
r.encoding='utf-8'
html_str=r.text
soup=BeautifulSoup(html_str,'lxml',from_encoding='utf-8')
'''
print soup.prettify() #格式化输出

#tag标签对象
print soup.title #抽取title
print soup.a #抽取a
print soup.p #抽取p
#Tag属性 name和attributes
print soup.name
print soup.title.name
print soup.p['id']
print soup.p.get('id')
print soup.p.attrs

#NavigableString对象
print soup.a.string
print type(soup.a.string)

#BeatifulSoup对象  soup就是一个BS对象
#Comment对象
print soup.a.string
print type(soup.a.string)

#遍历文档树
print soup.head.contents #所有子节点
print len(soup.head.contents)#子节点个数
print soup.head.contents[0].string
for child in soup.head.children:   #.child返回一个迭代器
    print child
for child in soup.head.descendants: #.descendants对所有子孙节点进行迭代
    print child


print soup.head.string
print soup.title.string
print soup.html.string
for string in soup.strings:
    print repr(string).decode('unicode_escape')
for string in soup.stripped_strings:
    print repr(string).decode('unicode_escape')
'''
#父节点
print soup.title.parent
#使用方法和child一样
#兄弟节点
print soup.p.next_sibling   #下一个兄弟节点
print soup.p.prev_sibling   #上一个兄弟节点
for sibling in soup.a.next_siblings:
    print repr(sibling)
#前后节点   .next_element .previous_element
#前后节点遍历 .next_elemnts  .previous_elements  迭代器
