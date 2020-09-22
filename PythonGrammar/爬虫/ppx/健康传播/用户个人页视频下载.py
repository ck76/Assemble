import json
import urllib
from urllib.error import HTTPError

import requests

# TODO 换cookie和url，存储路径，已下载目录txt路径，即可
# (origin)video_download
# 0插眼
# 1健康传播
# 2找春风
# 3绿色观察
# 4长寿秘籍

path_save_0 = "/Volumes/TOSHIBA/ppx/插眼/"
path_save_1 = "/Volumes/TOSHIBA/ppx/健康传播/"
path_save_2 = "/Volumes/TOSHIBA/ppx/找春风/"
path_save_3 = "/Volumes/TOSHIBA/ppx/绿色观察/"
path_save_4 = "/Volumes/TOSHIBA/ppx/长寿秘籍/"
path_save_5 = ""
path_save_6 = ""
# 目标视频存储位置
path_save_s = [path_save_0, path_save_1, path_save_2, path_save_3, path_save_4, path_save_5, path_save_6, ]

init_url_0 = "https://is.snssdk.com/bds/ward/list/?iid=2374555398325096&resolution=1242*2208&os_version=13.5.1&app_name=super&channel=App%20Store&idfa=1ABF0A44-4CBE-4191-B8E6-154836171658&device_platform=iphone&mac_address=02:00:00:00:00:00&vid=86A0335D-BB60-42CC-A461-72D1D67C6DE1&openudid=01942689b4d6f20e58ba3abb334a86fcf32d187c&device_type=iPhone%207%20Plus&idfv=86A0335D-BB60-42CC-A461-72D1D67C6DE1&version_code=3.0.6&ac=WIFI&device_id=2673605010266535&aid=1319&update_version_code=30680&user_id=179942927110947&count=20"
init_url_1 = "https://is.snssdk.com/bds/user/publish_list/?iid=2937491619330999&resolution=1242*2208&os_version=13.5.1&app_name=super&channel=App%20Store&idfa=6E007FDB-BEAC-493A-B75D-B45F76AEA6BD&device_platform=iphone&mac_address=02:00:00:00:00:00&vid=6248603F-E50C-444D-B928-543FB93C1F8C&openudid=01942689b4d6f20e58ba3abb334a86fcf32d187c&device_type=iPhone%207%20Plus&idfv=6248603F-E50C-444D-B928-543FB93C1F8C&version_code=2.9.8&ac=WIFI&device_id=2673605010266535&aid=1319&update_version_code=29880&count=20&user_id=1591688795264663&api_version=1&direction=1"
init_url_2 = "https://is.snssdk.com/bds/user/publish_list/?iid=2374555398325096&resolution=1242*2208&os_version=13.5.1&app_name=super&channel=App%20Store&idfa=1ABF0A44-4CBE-4191-B8E6-154836171658&device_platform=iphone&mac_address=02:00:00:00:00:00&vid=86A0335D-BB60-42CC-A461-72D1D67C6DE1&openudid=01942689b4d6f20e58ba3abb334a86fcf32d187c&device_type=iPhone%207%20Plus&idfv=86A0335D-BB60-42CC-A461-72D1D67C6DE1&version_code=3.0.6&ac=WIFI&device_id=2673605010266535&aid=1319&update_version_code=30680&count=20&user_id=4358067917166531&api_version=1&direction=1"
init_url_3 = "https://is.snssdk.com/bds/user/publish_list/?iid=2374555398325096&resolution=1242*2208&os_version=13.5.1&app_name=super&channel=App%20Store&idfa=1ABF0A44-4CBE-4191-B8E6-154836171658&device_platform=iphone&mac_address=02:00:00:00:00:00&vid=86A0335D-BB60-42CC-A461-72D1D67C6DE1&openudid=01942689b4d6f20e58ba3abb334a86fcf32d187c&device_type=iPhone%207%20Plus&idfv=86A0335D-BB60-42CC-A461-72D1D67C6DE1&version_code=3.0.6&ac=WIFI&device_id=2673605010266535&aid=1319&update_version_code=30680&count=20&user_id=6058032285&api_version=1&direction=1"
init_url_4 = "https://is.snssdk.com/bds/user/publish_list/?iid=2374555398325096&resolution=1242*2208&os_version=13.5.1&app_name=super&channel=App%20Store&idfa=1ABF0A44-4CBE-4191-B8E6-154836171658&device_platform=iphone&mac_address=02:00:00:00:00:00&vid=86A0335D-BB60-42CC-A461-72D1D67C6DE1&openudid=01942689b4d6f20e58ba3abb334a86fcf32d187c&device_type=iPhone%207%20Plus&idfv=86A0335D-BB60-42CC-A461-72D1D67C6DE1&version_code=3.0.6&ac=WIFI&device_id=2673605010266535&aid=1319&update_version_code=30680&count=20&user_id=1591688795264663&api_version=1&direction=1"
init_url_5 = ""
init_url_6 = ""
# url
init_url_s = [init_url_0, init_url_1, init_url_2, init_url_3, init_url_4, init_url_5, init_url_6, ]

path_yixiazai_0 = "/Volumes/TOSHIBA/ppx/插眼.txt"
path_yixiazai_1 = "/Volumes/TOSHIBA/ppx/健康传播.txt"
path_yixiazai_2 = "/Volumes/TOSHIBA/ppx/找春风.txt"
path_yixiazai_3 = "/Volumes/TOSHIBA/ppx/绿色观察.txt"
path_yixiazai_4 = "/Volumes/TOSHIBA/ppx/长寿秘籍.txt"
path_yixiazai_5 = ""
path_yixiazai_6 = ""

# 已下载的目录文件
path_yixiazai_s = [path_yixiazai_0, path_yixiazai_1, path_yixiazai_2, path_yixiazai_3, path_yixiazai_4, path_yixiazai_5,
                   path_yixiazai_6, ]
cookie = '''odin_tt=086849e00d3f955d5541126c9a7dec7ec2db27557fdff128f543fda2466a825f2b1ee2b9585686725c960c1e409df588c405e4b8b8be5754b445f00e4af92c8d;d_ticket=5f8fc87635be7acc88e9a5708a3f046607d02;sid_guard=158c6ffe4aa1c03f4d8eef9c7487c6a0%7C1599353104%7C5184000%7CThu%2C+05-Nov-2020+00%3A45%3A04+GMT;uid_tt=0b8e14f094b02cee966fad4d20de14af;uid_tt_ss=0b8e14f094b02cee966fad4d20de14af;sid_tt=158c6ffe4aa1c03f4d8eef9c7487c6a0;sessionid=158c6ffe4aa1c03f4d8eef9c7487c6a0;sessionid_ss=158c6ffe4aa1c03f4d8eef9c7487c6a0;install_id=2374555398325096;ttreq=1$5e844322393483f3a1d4e2d0944a149cc9273d6f'''
cookie_dict = {
    "odin_tt": "086849e00d3f955d5541126c9a7dec7ec2db27557fdff128f543fda2466a825f2b1ee2b9585686725c960c1e409df588c405e4b8b8be5754b445f00e4af92c8d",
    "d_ticket": "5f8fc87635be7acc88e9a5708a3f046607d02",
    "sid_guard": "158c6ffe4aa1c03f4d8eef9c7487c6a0%7C1599353104%7C5184000%7CThu%2C+05-Nov-2020+00%3A45%3A04+GMT",
    "uid_tt": "0b8e14f094b02cee966fad4d20de14af",
    "uid_tt_ss": "0b8e14f094b02cee966fad4d20de14af",
    "sid_t": "158c6ffe4aa1c03f4d8eef9c7487c6a0",
    "sessionid": "158c6ffe4aa1c03f4d8eef9c7487c6a0",
    "sessionid_ss": "158c6ffe4aa1c03f4d8eef9c7487c6a0",
    "install_id": "2374555398325096",
    "ttreq": "1$5e844322393483f3a1d4e2d0944a149cc9273d6f",
}
# headers = {
#     # 'User-Agent': "Super 3.0.6 rv:3.0.6.80 (iPhone; iOS 13.5.1; zh_CN) Cronet",
#     # 'Cookie': "odin_tt=086849e00d3f955d5541126c9a7dec7ec2db27557fdff128f543fda2466a825f2b1ee2b9585686725c960c1e409df588c405e4b8b8be5754b445f00e4af92c8d;d_ticket=5f8fc87635be7acc88e9a5708a3f046607d02;sid_guard=158c6ffe4aa1c03f4d8eef9c7487c6a0%7C1599353104%7C5184000%7CThu%2C+05-Nov-2020+00%3A45%3A04+GMT;uid_tt=0b8e14f094b02cee966fad4d20de14af;uid_tt_ss=0b8e14f094b02cee966fad4d20de14af;sid_tt=158c6ffe4aa1c03f4d8eef9c7487c6a0;sessionid=158c6ffe4aa1c03f4d8eef9c7487c6a0;sessionid_ss=158c6ffe4aa1c03f4d8eef9c7487c6a0;install_id=2374555398325096;ttreq=1$5e844322393483f3a1d4e2d0944a149cc9273d6f",
#     # "Cookie": "sessionid=158c6ffe4aa1c03f4d8eef9c7487c6a0;sessionid_ss=158c6ffe4aa1c03f4d8eef9c7487c6a0",
#     # "Cookie": cookie,
#     # "x-tt-token": "00158c6ffe4aa1c03f4d8eef9c7487c6a0d2b52ee1884e982c32b18e9d5172737e44ec74a178c431f10f741b97e487655836",
#     # "x-ss-cookie": "install_id=2374555398325096;ttreq=1$5e844322393483f3a1d4e2d0944a149cc9273d6f;d_ticket=5f8fc87635be7acc88e9a5708a3f046607d02;odin_tt=086849e00d3f955d5541126c9a7dec7ec2db27557fdff128f543fda2466a825f2b1ee2b9585686725c960c1e409df588c405e4b8b8be5754b445f00e4af92c8d;sessionid=158c6ffe4aa1c03f4d8eef9c7487c6a0;sessionid_ss=158c6ffe4aa1c03f4d8eef9c7487c6a0;sid_guard=158c6ffe4aa1c03f4d8eef9c7487c6a0%7C1599353104%7C5184000%7CThu%2C+05-Nov-2020+00%3A45%3A04+GMT;sid_tt=158c6ffe4aa1c03f4d8eef9c7487c6a0;uid_tt=0b8e14f094b02cee966fad4d20de14af;uid_tt_ss=0b8e14f094b02cee966fad4d20de14af"
# }
headers = {
    "Host": "iu.snssdk.com",
    "Cookie": "odin_tt=086849e00d3f955d5541126c9a7dec7ec2db27557fdff128f543fda2466a825f2b1ee2b9585686725c960c1e409df588c405e4b8b8be5754b445f00e4af92c8d; d_ticket=5f8fc87635be7acc88e9a5708a3f046607d02; sid_guard=158c6ffe4aa1c03f4d8eef9c7487c6a0%7C1599353104%7C5184000%7CThu%2C+05-Nov-2020+00%3A45%3A04+GMT; uid_tt=0b8e14f094b02cee966fad4d20de14af; uid_tt_ss=0b8e14f094b02cee966fad4d20de14af; sid_tt=158c6ffe4aa1c03f4d8eef9c7487c6a0; sessionid=158c6ffe4aa1c03f4d8eef9c7487c6a0; sessionid_ss=158c6ffe4aa1c03f4d8eef9c7487c6a0; install_id=2374555398325096; ttreq=1$5e844322393483f3a1d4e2d0944a149cc9273d6f",
    "x-tt-token": "00158c6ffe4aa1c03f4d8eef9c7487c6a0d2b52ee1884e982c32b18e9d5172737e44ec74a178c431f10f741b97e487655836",
    "x-ss-cookie": "install_id=2374555398325096; ttreq=1$5e844322393483f3a1d4e2d0944a149cc9273d6f; d_ticket=5f8fc87635be7acc88e9a5708a3f046607d02; odin_tt=086849e00d3f955d5541126c9a7dec7ec2db27557fdff128f543fda2466a825f2b1ee2b9585686725c960c1e409df588c405e4b8b8be5754b445f00e4af92c8d; sessionid=158c6ffe4aa1c03f4d8eef9c7487c6a0; sessionid_ss=158c6ffe4aa1c03f4d8eef9c7487c6a0; sid_guard=158c6ffe4aa1c03f4d8eef9c7487c6a0%7C1599353104%7C5184000%7CThu%2C+05-Nov-2020+00%3A45%3A04+GMT; sid_tt=158c6ffe4aa1c03f4d8eef9c7487c6a0; uid_tt=0b8e14f094b02cee966fad4d20de14af; uid_tt_ss=0b8e14f094b02cee966fad4d20de14af",
    "tt-request-time": "1600768307278",
    "user-agent": "Super 3.0.6 rv:3.0.6.80 (iPhone; iOS 13.5.1; zh_CN) Cronet",
    "sdk-version": "2",
    "passport-sdk-version": "5.12.0",
    "x-ss-dp": "1319",
    "x-tt-trace-id": "00-b539f1c50d97fa12ce819a7d46e70527-b539f1c50d97fa12-01",
    "x-khronos": "1600768304",
    "x-gorgon": "8402404700007b2b225643b32ce0e6f220f39e992a3287b79169"
}


def get_download_urls(path_save, init_url, yixiazai, origin_video_download_urls, origin_video_id_s):
    print(path_save)
    print(init_url)
    r = requests.get(init_url, headers=headers)
    print(r.status_code)
    r_json = json.loads(r.text)
    data_s = r_json.get("data").get("data")
    for cell in data_s:
        origin_video_download = cell.get("item").get("origin_video_download").get("url_list")[0].get("url")
        print(origin_video_download)
        origin_video_id = cell.get("item").get("origin_video_id")
        # 【带水印】
        # video_download = cell.get("item").get("video").get("video_download").get("url_list")[0].get("url")
        origin_video_download_urls.append(origin_video_download)
        origin_video_id_s.append(origin_video_id)
        try:
            if yixiazai.__contains__(str(origin_video_id)):
                print("已存在：" + origin_video_id)
                continue
            f = urllib.request.urlopen(origin_video_download)
            data = f.read()
            # 存储位置可自定义
            with open(path_save + str(origin_video_id) + ".mp4", 'wb') as code:
                code.write(data)
        except HTTPError:
            print(origin_video_download)
    cursor = r_json["data"].get("cursor")
    if cursor.get("has_more") == True:
        cursor = cursor.get("loadmore_cursor")
        init_url = init_url.replace("direction=1", "direction=2") + "&cursor=" + str(cursor)
        print(init_url)
        get_download_urls(path_save, init_url, yixiazai, origin_video_download_urls, origin_video_id_s)


def start():
    origin_video_download_urls = []
    origin_video_id_s = []
    yixiazai = []
    path_yixiazai = ""
    try:
        print()
        for index in range(0, len(path_save_s)):
            if index == 0 :
                continue
            if index == 1 :
                continue
            path_save = path_save_s[index]
            if path_save == "":
                continue
            path_yixiazai = path_yixiazai_s[index]
            init_url = init_url_s[index]
            temp = open(path_yixiazai).readlines()
            for item in temp:
                yixiazai.append(item.split("--")[0])

            get_download_urls(path_save, init_url, yixiazai, origin_video_download_urls, origin_video_id_s)

            # 保存
            with open(path_yixiazai, "w+") as file:
                for i in range(0, len(origin_video_id_s)):
                    file.writelines(origin_video_id_s[i] + "--" + origin_video_download_urls[i] + "\n")
                file.close()
            print("ok")
    finally:
        # 保存
        print("finally:xxxxxxx")
        with open(path_yixiazai, "w+") as file:
            for i in range(0, len(origin_video_id_s)):
                file.writelines(origin_video_id_s[i] + "--" + origin_video_download_urls[i] + "\n")
            file.close()


start()
