import json
import urllib
from urllib.error import HTTPError
import certifi
import cryptography

import requests

headers = {
    'Cookie': 'sessionid=158c6ffe4aa1c03f4d8eef9c7487c6a0',
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
}
熟人志 = "https://is.snssdk.com/bds/user/publish_list/?iid=2374555398325096&resolution=1242*2208&os_version=13.5.1&app_name=super&channel=App%20Store&idfa=1ABF0A44-4CBE-4191-B8E6-154836171658&device_platform=iphone&mac_address=02:00:00:00:00:00&vid=86A0335D-BB60-42CC-A461-72D1D67C6DE1&openudid=01942689b4d6f20e58ba3abb334a86fcf32d187c&device_type=iPhone%207%20Plus&idfv=86A0335D-BB60-42CC-A461-72D1D67C6DE1&version_code=3.0.6&ac=WIFI&device_id=2673605010266535&aid=1319&update_version_code=30680&count=20&user_id=1947990820141172&api_version=1&direction=1"
ss="https://is.snssdk.com/bds/user/user_profile/?iid=2374555398325096&resolution=1242*2208&os_version=13.5.1&app_name=super&channel=App%20Store&idfa=1ABF0A44-4CBE-4191-B8E6-154836171658&device_platform=iphone&mac_address=02:00:00:00:00:00&vid=86A0335D-BB60-42CC-A461-72D1D67C6DE1&openudid=01942689b4d6f20e58ba3abb334a86fcf32d187c&device_type=iPhone%207%20Plus&idfv=86A0335D-BB60-42CC-A461-72D1D67C6DE1&version_code=3.0.6&ac=WIFI&device_id=2673605010266535&aid=1319&update_version_code=30680&user_id=1226655901687588"
url = "https://is.snssdk.com/bds/ward/list/?iid=2374555398325096&resolution=1242*2208&os_version=13.5.1&app_name=super&channel=App%20Store&idfa=1ABF0A44-4CBE-4191-B8E6-154836171658&device_platform=iphone&mac_address=02:00:00:00:00:00&vid=86A0335D-BB60-42CC-A461-72D1D67C6DE1&openudid=01942689b4d6f20e58ba3abb334a86fcf32d187c&device_type=iPhone%207%20Plus&idfv=86A0335D-BB60-42CC-A461-72D1D67C6DE1&version_code=3.0.6&ac=WIFI&device_id=2673605010266535&aid=1319&update_version_code=30680&user_id=179942927110947&count=20"

r = requests.get(熟人志, headers=headers)
r.encoding="utf-8"
# print(r.json())
print(r.content)
print(r.text)
