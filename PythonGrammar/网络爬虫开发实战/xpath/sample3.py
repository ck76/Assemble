import requests
from lxml import etree

jlpt=requests.get('https://share.jiemo.net/nSeries/grammarShare?id=3')
print(jlpt.text)
html = etree.parse('./test.html', etree.HTMLParser())
print(type(html))
result = html.xpath('//li')
print(result)
print(result[0])
