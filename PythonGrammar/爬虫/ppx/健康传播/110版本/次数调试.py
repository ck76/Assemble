import json
import urllib
from urllib.error import HTTPError
import certifi
import cryptography
# import 用户个人页视频下载
import requests

s = '''
d_ticket=a706138bd0b723461a61380db690e82a07d02; odin_tt=b8c25a7ca2d6230a0d921425e4d4753477ad0590b016d2508a67e834af32ae445fd6aff17b737783a3ae3f3d0e3e259282a1634fff3009101bc62b51931ced92; sid_guard=2701e191636e1853e1785b4648783c3c%7C1601115548%7C5184000%7CWed%2C+25-Nov-2020+10%3A19%3A08+GMT; uid_tt=f249d37500a1aa64e439a06cdb719b66; sid_tt=2701e191636e1853e1785b4648783c3c; sessionid=2701e191636e1853e1785b4648783c3c
d_ticket=a706138bd0b723461a61380db690e82a07d02; odin_tt=b8c25a7ca2d6230a0d921425e4d4753477ad0590b016d2508a67e834af32ae445fd6aff17b737783a3ae3f3d0e3e259282a1634fff3009101bc62b51931ced92; sessionid=2701e191636e1853e1785b4648783c3c; sid_guard=2701e191636e1853e1785b4648783c3c%7C1601115548%7C5184000%7CWed%2C+25-Nov-2020+10%3A19%3A08+GMT; sid_tt=2701e191636e1853e1785b4648783c3c; uid_tt=f249d37500a1aa64e439a06cdb719b66


'''
headers = {
    "Host": "api.ribaoapi.com",
    "Cookie": "d_ticket=a706138bd0b723461a61380db690e82a07d02; odin_tt=b8c25a7ca2d6230a0d921425e4d4753477ad0590b016d2508a67e834af32ae445fd6aff17b737783a3ae3f3d0e3e259282a1634fff3009101bc62b51931ced92; sid_guard=2701e191636e1853e1785b4648783c3c%7C1601115548%7C5184000%7CWed%2C+25-Nov-2020+10%3A19%3A08+GMT; uid_tt=f249d37500a1aa64e439a06cdb719b66; sid_tt=2701e191636e1853e1785b4648783c3c; sessionid=2701e191636e1853e1785b4648783c3c",
    "x-ss-cookie": "d_ticket=a706138bd0b723461a61380db690e82a07d02; odin_tt=b8c25a7ca2d6230a0d921425e4d4753477ad0590b016d2508a67e834af32ae445fd6aff17b737783a3ae3f3d0e3e259282a1634fff3009101bc62b51931ced92; sessionid=2701e191636e1853e1785b4648783c3c; sid_guard=2701e191636e1853e1785b4648783c3c%7C1601115548%7C5184000%7CWed%2C+25-Nov-2020+10%3A19%3A08+GMT; sid_tt=2701e191636e1853e1785b4648783c3c; uid_tt=f249d37500a1aa64e439a06cdb719b66",
    "tt-request-time": "1601115636352",
    "user-agent": "Super 1.1.0 rv:1.1.0.6 (iPhone; iOS 13.5.1; zh_CN) Cronet",
}
熟人志="http://api.ribaoapi.com/bds/user/userfeed/?iid=3993043734112957&resolution=1242*2208&app_name=super&channel=App%20Store&device_platform=iphone&idfa=1ABF0A44-4CBE-4191-B8E6-154836171658&vid=16669D53-CE1F-4081-991A-1EDCD1888DE8&openudid=be5d560c284b36c0aedb650d91fcc14095e13e7e&device_type=iPhone%207%20Plus&idfv=16669D53-CE1F-4081-991A-1EDCD1888DE8&device_id=2673605010266535&ac=WIFI&version_code=1.1.0&os_version=13.5.1&aid=1319&user_id=104338013259&direction=1&list_type=0&mas=00b9272009f90a3159d252ce394c242525e78d2fdb1b10191bf797&as=a2d5e1a644af8f059f1384&ts=1601115636"

class RequestSpider(object):
    def __init__(self):
        url = 熟人志
        self.response = requests.get(url, headers=headers)

    def run(self):
        print("text: " + self.response.text)
        data = self.response.content
        print(data)

        # 1.获取请求头
        request_headers = self.response.request.headers
        print(request_headers)

        # 2.获取相应头
        coderesponse_headers = self.response.headers
        print(coderesponse_headers)

        # 3.响应状态码
        code = self.response.status_code
        print(code)

        # 4. 请求的cookie 注意写法
        request_cookie = self.response.request._cookies
        print(request_cookie)

        # 5. 响应的cookie
        response_cookie = self.response.cookies
        print(response_cookie)


RequestSpider().run()
