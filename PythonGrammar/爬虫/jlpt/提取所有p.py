import json

# 1-207     1-31
# 208-362   32-64
# 363-521   65-90
# 522-640   91-119
# 641-793   120-137 666 -794-667

#
import os
import requests
import urllib
from lxml import etree
import os

path = "/Users/chengkun/workspace/iBook/语言学/日语/芥末语法1-792/"
mulu = ["语法内容", "解说", "接続", "例文", "注意点", "相关文法"]

all_p = {794: {"语法内容": ["hhhhh"], "解说": ["hhhhh"]}}

print(all_p)
result = []
for item in all_p:
    tag = ""
    if item in mulu:
        print()
        tag = item
for i in range(1, 795):
    all_p[i] = {}

for i in range(1, 795):
    # kari_title = all_p[i]

    kari = {}
    kari_texts = []
    current_title = ""
    current_p_text = []
    html_path = path + str(i) + ".html"
    # parse_html = etree.HTML(r.text)
    parse_html = etree.parse(html_path, etree.HTMLParser())
    element_s = parse_html.xpath("//div[@class='grammar-content']/*")
    # 进行一次循环，完成一个html页面的提取
    for element in element_s:
        if element.attrib == "span":
            # 清空操作
            current_title = element.text
            current_p_text=[]
            if kari.__contains__(current_title):
                pass
            else:
                kari[current_title] = []

        if element.attrib == "p":
            current_p_text.append(element.text)

    # print(span_s)

    break
    # p_s = parse_html.xpath("//p/text()")
    all_p[i] = kari

print(all_p)

# res = dom_tree.xpath('//li')[5]
# res1 = html.tostring(res)
# res2 = HTMLParser().unescape(res1.decode('utf-8'))
# print(res.attrib)
# print(res.text)
