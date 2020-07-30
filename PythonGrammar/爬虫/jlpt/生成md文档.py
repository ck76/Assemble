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

html_path = "/Users/chengkun/workspace/iBook/语言学/日语/芥末语法1-792/"
json_list = os.listdir("./json/")

print(json_list)
for json_item in json_list:
    n1_json = open("./json/" + json_item).read()
    n1 = json.loads(n1_json)
    print(n1)
    data = n1.get("data")
    print(data[0].get("level"))
    for item in data:
        # print(item.get("id"))
        title = item.get("title")
        print(title)
        grammerList = item.get("grammerList")
        for grammer_item in grammerList:
            grammar = grammer_item.get("grammar")
            grammer_id = grammer_item.get("id")
            print(grammer_id)
            parse_html = etree.parse(html_path + str(grammer_id) + ".html", etree.HTMLParser())
            span_s = parse_html.xpath("//span/text()")
            p_s = parse_html.xpath("//p/text()")
            # ['语法内容', '解说', '接続', '例文', '注意点', ' 相关文法']
            print(span_s)

            # print(p_s)
            with open("jlpt.md", 'w') as code:
                pass
                for i in range(0,len(span_s)):
                    if span_s[i]=="相关文法":

                        continue
                    code.write(span_s[i]+"\n")
                    code.write(p_s[i].replace("\n", "").replace("                ", "").replace("            ", ""))
                    if
                    code.write("\n")
                # for item in span_s:
                #     code.write(item)
                # for item in p_s:
                #     code.write(item.replace("\n", "").replace("                ", "").replace("            ", ""))
                #     code.write("\n")
                    # print(item.replace("\n",""))
                # code.write(span_s)
                # code.write(p_s)


"""
### N1

#### 伴随、非伴随

##### **~かたがた**

```c
//接续
N+かたがた
```

```c
//解说
表示某行为兼具两个目的。“顺便……”。
```

```c
//例文
①散歩かたがた駅前の本屋に行きました。
  ／散步的时候顺便去了趟车站附近的书店。
②先生が引っ越したというので、挨拶かたがたお菓子を持ってお宅を訪問することにした。
  ／听说老师搬家了，我决定去问候一下老师，带了些点心去老师家拜访。
```

```c
//注意点
①是较为正式的表达，与「～を兼ねて」相同。
②通常与「お見舞い」「ご挨拶」「お礼」「お詫び」等词连用。
```
"""