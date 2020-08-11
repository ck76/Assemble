import os
from urllib.error import HTTPError

import requests
import urllib
from lxml import etree
import os
import json

path = "/Users/chengkun/Downloads/ppx/"
os.chdir(path)
url = "http://v3-ppx.ixigua.com/9b45ef4a808db841b6e37c54822dc1ca/5f31590d/video/m/2206dc2b4a9161e420786ff773859abd7cc1166304b4000066aef1a11a65/?a=1319\u0026br=1593\u0026bt=531\u0026cr=0\u0026cs=0\u0026dr=3\u0026ds=3\u0026er=\u0026l=20200810212615010014048140041E1598\u0026lr=\u0026mime_type=video_mp4\u0026qs=0\u0026rc=amd5dmU7dTxkdTMzaWYzM0ApZTs5ZWZkO2VkN2RnOzpmN2ctcGI1ai1waW9fLS00MS9zczIzMTIzMjQzYWE2LWBfYTQ6Yw%3D%3D\u0026vl=\u0026vr="

try:
    f = urllib.request.urlopen(url)
    data = f.read()
    # 存储位置可自定义
    with open("result_name"+".mp4", 'wb') as code:
        code.write(data)
except HTTPError:
    print(url)
except  UnicodeEncodeError:
    print(url)
