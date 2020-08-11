from selenium import webdriver#导入库
browser = webdriver.Chrome()#声明浏览器
url = 'http://ds.addsxz.com/123ddtp.pdf?attname='
browser.get(url)#打开浏览器预设网址
print(browser.page_source)#打印网页源代码
browser.close()#关闭浏览器

import urllib
import urllib.request
import re
import os

url='http://ds.addsxz.com/123ddtp.pdf?attname='
u = urllib.request.urlopen(url)
urllib.urlretrieve(url,"ss.pdf")
print(u)
# f = open("file_name.pdf", 'wb')
