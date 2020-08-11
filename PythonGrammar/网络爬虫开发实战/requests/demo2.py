# coding: gb2312
#!/usr/bin/env python

# http://www.j9p.com/down/525808.html
# http://www.j9p.com/down/517525.html
import requests
import urllib
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
}
# r = requests.get('http://ds.addsxz.com/123ddtp.pdf',headers=headers)
# r.encoding='UTF-8'
# print(r.text)
# with open("result.pdf", "w") as f:
#     f.writelines(str(r.content))

# for i in range(1,153):
#     link="http://www.j9p.com/class/r_16_"+str(i)+".html"
#     print(link)

r = requests.get('http://ds.addsxz.com/123ddtp.pdf',headers=headers)

import urllib.request

print("downloading with urllib")
url = 'http://ds.addsxz.com/123ddtp.pdf'
f = urllib.request.urlopen(url)
data = f.read()
# 存储位置可自定义
for i in range(1,10):
    with open("sss"+str(i)+".pdf", 'wb') as code:
        code.write(data)