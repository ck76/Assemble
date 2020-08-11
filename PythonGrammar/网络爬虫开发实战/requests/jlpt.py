import requests
from urllib.parse import urlsplit
import os

os.chdir("/Users/chengkun/workspace/iBook/语言学/日语/芥末语法1-792/")

# https://share.jiemo.net/nSeries/grammarShare?id=1
# https://share.jiemo.net/nSeries/grammarShare?id=792
r = requests.get('https://share.jiemo.net/nSeries/grammarShare?id=1')

print(r.text)

print(urlsplit('https://share.jiemo.net/nSeries/grammarShare?id=8'))

for i in range(1, 793):
    r = requests.get("https://share.jiemo.net/nSeries/grammarShare?id=" + str(i))
    with open(str(i) + ".html", "w") as f:
        f.writelines(r.text)
