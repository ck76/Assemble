# coding: gb2312
# !/usr/bin/env python

# http://www.j9p.com/down/525808.html
# http://www.j9p.com/down/517525.html
# /Users/chengkun/workspace/iBook/爬虫/
import os
import requests
import urllib
from lxml import etree
enter_command = "\r\n"
os.chdir("/Users/chengkun/workspace/iBook/爬虫/奥丁html/")
htmls = os.listdir()
htmls.sort()
print(htmls)
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
}
# 共163页
result=[]
for html in htmls:
    if html == ".DS_Store":
        continue
    print(html)
    # r = requests.get("http://www.addsxz.com/html/list_6_" + str(page) + ".html", headers=headers)
    # r.encoding = 'UTF-8'
    # with open("list_6_" + str(page) + ".html","w") as file:
    #     file.write(r.text)

    parse_html = etree.parse(html, etree.HTMLParser())
    title = parse_html.xpath("//div[@class='block']/h2/a/text()")
    for line in title:
        result.append(str(line))
    print(str(title))
with open("奥丁所有书籍.txt", 'w') as fout:
    for item in result:
        fout.writelines(item)
        fout.writelines(enter_command)
# r = requests.get('http://www.addsxz.com/html/list_6_2.html',headers=headers)
# r.encoding='UTF-8'
# print(r.text)


# for i in range(1,153):
#     link="http://www.j9p.com/class/r_16_"+str(i)+".html"
#     print(link)

# r = requests.get('http://ds.addsxz.com/123ddtp.pdf',headers=headers)

# import urllib.request
#
# print("downloading with urllib")
# url = 'http://ds.addsxz.com/123ddtp.pdf'
# f = urllib.request.urlopen(url)
# data = f.read()
# # 存储位置可自定义
# with open("sss.pdf", 'wb') as code:
#     code.write(data)


"""删除第一行"""

#
# def del_firstline(filename):
#     os.chdir("/Users/chengkun/workspace/iBook/爬虫/奥丁原/")
#     with open(filename, 'r') as fin:
#         data = fin.read().splitlines(True)
#     os.chdir("/Users/chengkun/workspace/iBook/爬虫/奥丁html/")
#     with open(filename, 'w') as fout:
#         fout.writelines(data[1:])
#     os.chdir("/Users/chengkun/workspace/iBook/爬虫/奥丁原/")
#
#
# # /Users/chengkun/workspace/iBook/爬虫/奥丁html/
# # /Users/chengkun/workspace/iBook/爬虫/奥丁原/
# os.chdir("/Users/chengkun/workspace/iBook/爬虫/奥丁原/")
# files = os.listdir()
# for file in files:
#     del_firstline(file)
