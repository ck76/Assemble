import requests
from lxml import etree
import requests
text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''
jlpt=requests.get('https://share.jiemo.net/nSeries/grammarShare?id=3')
# print(jlpt.text)
html = etree.HTML(jlpt.text)
# html = etree.HTML(text)
result = etree.tostring(html)
# print(result.decode('utf-8'))

li=html.xpath('//h1//span//text()')
print(li)
texts=html.xpath('//p//text()')
print(texts)