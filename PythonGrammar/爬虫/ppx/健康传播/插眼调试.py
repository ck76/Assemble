import json
import urllib
from urllib.error import HTTPError
import certifi
import cryptography

import requests
headers = {
    "Host": "is.snssdk.com",
    # "Cookie": "odin_tt=086849e00d3f955d5541126c9a7dec7ec2db27557fdff128f543fda2466a825f2b1ee2b9585686725c960c1e409df588c405e4b8b8be5754b445f00e4af92c8d; d_ticket=5f8fc87635be7acc88e9a5708a3f046607d02; sid_guard=158c6ffe4aa1c03f4d8eef9c7487c6a0%7C1599353104%7C5184000%7CThu%2C+05-Nov-2020+00%3A45%3A04+GMT; uid_tt=0b8e14f094b02cee966fad4d20de14af; uid_tt_ss=0b8e14f094b02cee966fad4d20de14af; sid_tt=158c6ffe4aa1c03f4d8eef9c7487c6a0; sessionid=158c6ffe4aa1c03f4d8eef9c7487c6a0; sessionid_ss=158c6ffe4aa1c03f4d8eef9c7487c6a0; install_id=2374555398325096; ttreq=1$5e844322393483f3a1d4e2d0944a149cc9273d6f",
    "Cookie": "odin_tt=086849e00d3f955d5541126c9a7dec7ec2db27557fdff128f543fda2466a825f2b1ee2b9585686725c960c1e409df588c405e4b8b8be5754b445f00e4af92c8d; d_ticket=5f8fc87635be7acc88e9a5708a3f046607d02; sid_guard=158c6ffe4aa1c03f4d8eef9c7487c6a0%7C1599353104%7C5184000%7CThu%2C+05-Nov-2020+00%3A45%3A04+GMT; uid_tt=0b8e14f094b02cee966fad4d20de14af; uid_tt_ss=0b8e14f094b02cee966fad4d20de14af; sid_tt=158c6ffe4aa1c03f4d8eef9c7487c6a0; sessionid=158c6ffe4aa1c03f4d8eef9c7487c6a0; sessionid_ss=158c6ffe4aa1c03f4d8eef9c7487c6a0; install_id=2374555398325096; ttreq=1$5e844322393483f3a1d4e2d0944a149cc9273d6f",
    "x-tt-token": "00158c6ffe4aa1c03f4d8eef9c7487c6a06e3c8a43680206e28de7a4277c8847ec1489eef72ab80aa4b50a96f145a84a558",
    "x-ss-cookie": "install_id=2374555398325096; ttreq=1$5e844322393483f3a1d4e2d0944a149cc9273d6f; d_ticket=5f8fc87635be7acc88e9a5708a3f046607d02; odin_tt=086849e00d3f955d5541126c9a7dec7ec2db27557fdff128f543fda2466a825f2b1ee2b9585686725c960c1e409df588c405e4b8b8be5754b445f00e4af92c8d; sessionid=158c6ffe4aa1c03f4d8eef9c7487c6a0; sessionid_ss=158c6ffe4aa1c03f4d8eef9c7487c6a0; sid_guard=158c6ffe4aa1c03f4d8eef9c7487c6a0%7C1599353104%7C5184000%7CThu%2C+05-Nov-2020+00%3A45%3A04+GMT; sid_tt=158c6ffe4aa1c03f4d8eef9c7487c6a0; uid_tt=0b8e14f094b02cee966fad4d20de14af; uid_tt_ss=0b8e14f094b02cee966fad4d20de14af",
    "tt-request-time": "1600951792975",
    # "user-agent": "Super 3.0.6 rv:3.0.6.80 (iPhone; iOS 13.5.1; zh_CN) Cronet",
    "user-agent": "Super 3.0.6 rv:3.0.6.80 (iPhone; iOS 13.5.1; zh_CN) Cronet",
    "sdk-version": "2",
    "passport-sdk-version": "5.12.0",
    "x-ss-dp": "1319",
    "x-tt-trace-id": "00-c029b6c70d97fa12ce819a71fe180527-c029b6c70d97fa12-01",
    "x-khronos": "1600951792",
    "x-gorgon": "8402a00200006406593d068d8d60974515802bd3cec1c9289c00"
}
# headers = {
#     'Cookie': 'sessionid=158c6ffe4aa1c03f4d8eef9c7487c6a0',
#     "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
# }
熟人志 = "https://is.snssdk.com/bds/user/publish_list/?iid=2374555398325096&resolution=1242*2208&os_version=13.5.1&app_name=super&channel=App%20Store&idfa=1ABF0A44-4CBE-4191-B8E6-154836171658&device_platform=iphone&mac_address=02:00:00:00:00:00&vid=86A0335D-BB60-42CC-A461-72D1D67C6DE1&openudid=01942689b4d6f20e58ba3abb334a86fcf32d187c&device_type=iPhone%207%20Plus&idfv=86A0335D-BB60-42CC-A461-72D1D67C6DE1&version_code=3.0.6&ac=WIFI&device_id=2673605010266535&aid=1319&update_version_code=30680&count=20&user_id=1947990820141172&api_version=1&direction=1"
ss="https://is.snssdk.com/bds/user/user_profile/?iid=2374555398325096&resolution=1242*2208&os_version=13.5.1&app_name=super&channel=App%20Store&idfa=1ABF0A44-4CBE-4191-B8E6-154836171658&device_platform=iphone&mac_address=02:00:00:00:00:00&vid=86A0335D-BB60-42CC-A461-72D1D67C6DE1&openudid=01942689b4d6f20e58ba3abb334a86fcf32d187c&device_type=iPhone%207%20Plus&idfv=86A0335D-BB60-42CC-A461-72D1D67C6DE1&version_code=3.0.6&ac=WIFI&device_id=2673605010266535&aid=1319&update_version_code=30680&user_id=1226655901687588"
url = "https://is.snssdk.com/bds/ward/list/?iid=2374555398325096&resolution=1242*2208&os_version=13.5.1&app_name=super&channel=App%20Store&idfa=1ABF0A44-4CBE-4191-B8E6-154836171658&device_platform=iphone&mac_address=02:00:00:00:00:00&vid=86A0335D-BB60-42CC-A461-72D1D67C6DE1&openudid=01942689b4d6f20e58ba3abb334a86fcf32d187c&device_type=iPhone%207%20Plus&idfv=86A0335D-BB60-42CC-A461-72D1D67C6DE1&version_code=3.0.6&ac=WIFI&device_id=2673605010266535&aid=1319&update_version_code=30680&user_id=179942927110947&count=20"

r = requests.get(熟人志, headers=headers)
r.encoding="utf-8"
# print(r.json())
# print(r.content)
# print(r.text)


class RequestSpider(object):
    def __init__(self):
        # url = 'https://www.baidu.com'
        url=熟人志
        # headers = {
        #     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
        # }
        self.response = requests.get(url, headers=headers)

    def run(self):
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