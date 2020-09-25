import time
import datetime
import os

url_1="curl -H 'Host: it.snssdk.com' -H 'Cookie: odin_tt=086849e00d3f955d5541126c9a7dec7ec2db27557fdff128f543fda2466a825f2b1ee2b9585686725c960c1e409df588c405e4b8b8be5754b445f00e4af92c8d; d_ticket=5f8fc87635be7acc88e9a5708a3f046607d02; sid_guard=158c6ffe4aa1c03f4d8eef9c7487c6a0%7C1599353104%7C5184000%7CThu%2C+05-Nov-2020+00%3A45%3A04+GMT; uid_tt=0b8e14f094b02cee966fad4d20de14af; uid_tt_ss=0b8e14f094b02cee966fad4d20de14af; sid_tt=158c6ffe4aa1c03f4d8eef9c7487c6a0; sessionid=158c6ffe4aa1c03f4d8eef9c7487c6a0; sessionid_ss=158c6ffe4aa1c03f4d8eef9c7487c6a0; install_id=2374555398325096; ttreq=1$5e844322393483f3a1d4e2d0944a149cc9273d6f' -H 'x-tt-token: 00158c6ffe4aa1c03f4d8eef9c7487c6a06e3c8a43680206e28de7a4277c8847ec1489eef72ab80aa4b50a96f145a84a558' -H 'x-ss-cookie: install_id=2374555398325096; ttreq=1$5e844322393483f3a1d4e2d0944a149cc9273d6f; d_ticket=5f8fc87635be7acc88e9a5708a3f046607d02; odin_tt=086849e00d3f955d5541126c9a7dec7ec2db27557fdff128f543fda2466a825f2b1ee2b9585686725c960c1e409df588c405e4b8b8be5754b445f00e4af92c8d; sessionid=158c6ffe4aa1c03f4d8eef9c7487c6a0; sessionid_ss=158c6ffe4aa1c03f4d8eef9c7487c6a0; sid_guard=158c6ffe4aa1c03f4d8eef9c7487c6a0%7C1599353104%7C5184000%7CThu%2C+05-Nov-2020+00%3A45%3A04+GMT; sid_tt=158c6ffe4aa1c03f4d8eef9c7487c6a0; uid_tt=0b8e14f094b02cee966fad4d20de14af; uid_tt_ss=0b8e14f094b02cee966fad4d20de14af' -H 'tt-request-time: 1601028484104' -H 'user-agent: Super 3.0.6 rv:3.0.6.80 (iPhone; iOS 13.5.1; zh_CN) Cronet' -H 'sdk-version: 2' -H 'passport-sdk-version: 5.12.0' -H 'x-ss-dp: 1319' -H 'x-tt-trace-id: 00-c4bbed7e0d97fa12ce819a7bf5510527-c4bbed7e0d97fa12-01' -H 'x-khronos: "

url_2="' -H 'x-gorgon: 840280af00008ab5697d7680721d4afab03aef45f6e4b9c71a59' --compressed 'https://it.snssdk.com/bds/user/publish_list/?iid=2374555398325096&resolution=1242*2208&os_version=13.5.1&app_name=super&channel=App%20Store&idfa=1ABF0A44-4CBE-4191-B8E6-154836171658&device_platform=iphone&mac_address=02:00:00:00:00:00&vid=86A0335D-BB60-42CC-A461-72D1D67C6DE1&openudid=01942689b4d6f20e58ba3abb334a86fcf32d187c&device_type=iPhone%207%20Plus&idfv=86A0335D-BB60-42CC-A461-72D1D67C6DE1&version_code=3.0.6&ac=WIFI&device_id=2673605010266535&aid=1319&update_version_code=30680&count=20&user_id=2334989129615431&api_version=1&direction=1'"
t = time.time()
print(t)  # 原始时间数据
print(int(t))  # 秒级时间戳
print(int(round(t * 1000)))  # 毫秒级时间戳
print(int(round(t * 1000000)))  # 微秒级时间戳
# 1601028984
# 1601026656# 秒级时间戳
# 1601028984135# 毫秒级时间戳
# 1601026657469
# for i in range(0, 10):
#     time.sleep(1)
#     t = time.time()
#     shijianchuo = int(t)
#     url=url_1+str(shijianchuo)+url_2
#     print(shijianchuo)
#     print(url)
#     print(os.system(url))
