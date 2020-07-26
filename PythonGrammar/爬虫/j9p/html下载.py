# http://www.j9p.com/class/182_11.html【互联网科技】
# http://www.j9p.com/class/183_35.html【文学艺术】
# http://www.j9p.com/class/184_19.html【经济管理】
# http://www.j9p.com/class/185_13.html【社会科学】
# http://www.j9p.com/class/187_12.html【文化历史】
# http://www.j9p.com/class/188_21.html【教程资料】
# http://www.j9p.com/class/189_34.html【生活百科】
# http://www.j9p.com/class/190_8.html【教育相关】
#
import os

import requests
from lxml import etree

base_addr = "http://www.j9p.com/class/"
enter_command = "\n"

os.chdir("./目录")


def download_catalog(leibie, page_count, name):
    result = []

    # os.chdir()
    for page in range(1, page_count + 1):
        url = base_addr + str(leibie) + "_" + str(page) + ".html"
        print(url)
        # r = requests.get(url)
        # r.encoding = 'gb2312'
        # print(r.text)
        parse_html = etree.parse(url, etree.HTMLParser())
        book_name = parse_html.xpath("//ul[@class='slist tabcon']/li[@class='item']//p[@class='name']/text()")
        print(book_name)
        for item in book_name:
            result.append(item)
        # with open("list_10_" + str(page) + ".html", "w") as file:
        #     file.write(r.text)

    # for html in os.listdir():
    #     if html == ".DS_Store":
    #         continue
    #     print(html)
    #     parse_html = etree.parse(html, etree.HTMLParser())
    #     title = parse_html.xpath("//div[@class='block']/h2/a/text()")
    #     for line in title:
    #         result.append(str(line))
    #     print(str(title))
    # with open(str(name) + "目录.txt", 'w') as fout:
    #     for item in result:
    #         fout.writelines(item)
    #         fout.writelines(enter_command)
    # with open(str("带序号") + str(name) + "目录.txt", 'w') as fout:
    #     count = 1
    #     for item in result:
    #         fout.writelines(str(count) + "：" + str(item))
    #         fout.writelines(enter_command)
    #         count = count + 1


download_catalog(182, 11, "互联网科技")
download_catalog(183, 35, "文学艺术")
download_catalog(184, 19, "经济管理")
download_catalog(185, 13, "社会科学")
download_catalog(187, 12, "文化历史")
download_catalog(188, 21, "教程资料")
download_catalog(189, 34, "生活百科")
download_catalog(190, 8, "教育相关")
