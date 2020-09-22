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

init_ur_0 = "https://is.snssdk.com/bds/ward/list/?iid=2374555398325096&resolution=1242*2208&os_version=13.5.1&app_name=super&channel=App%20Store&idfa=1ABF0A44-4CBE-4191-B8E6-154836171658&device_platform=iphone&mac_address=02:00:00:00:00:00&vid=86A0335D-BB60-42CC-A461-72D1D67C6DE1&openudid=01942689b4d6f20e58ba3abb334a86fcf32d187c&device_type=iPhone%207%20Plus&idfv=86A0335D-BB60-42CC-A461-72D1D67C6DE1&version_code=3.0.6&ac=WIFI&device_id=2673605010266535&aid=1319&update_version_code=30680&user_id=179942927110947&count=20"
init_url_1 = "https://is.snssdk.com/bds/user/publish_list/?iid=2937491619330999&resolution=1242*2208&os_version=13.5.1&app_name=super&channel=App%20Store&idfa=6E007FDB-BEAC-493A-B75D-B45F76AEA6BD&device_platform=iphone&mac_address=02:00:00:00:00:00&vid=6248603F-E50C-444D-B928-543FB93C1F8C&openudid=01942689b4d6f20e58ba3abb334a86fcf32d187c&device_type=iPhone%207%20Plus&idfv=6248603F-E50C-444D-B928-543FB93C1F8C&version_code=2.9.8&ac=WIFI&device_id=2673605010266535&aid=1319&update_version_code=29880&count=20&user_id=1591688795264663&api_version=1&direction=1"
init_url_2 = "https://is.snssdk.com/bds/user/publish_list/?iid=2374555398325096&resolution=1242*2208&os_version=13.5.1&app_name=super&channel=App%20Store&idfa=1ABF0A44-4CBE-4191-B8E6-154836171658&device_platform=iphone&mac_address=02:00:00:00:00:00&vid=86A0335D-BB60-42CC-A461-72D1D67C6DE1&openudid=01942689b4d6f20e58ba3abb334a86fcf32d187c&device_type=iPhone%207%20Plus&idfv=86A0335D-BB60-42CC-A461-72D1D67C6DE1&version_code=3.0.6&ac=WIFI&device_id=2673605010266535&aid=1319&update_version_code=30680&count=20&user_id=4358067917166531&api_version=1&direction=1"
init_url_3 = "https://is.snssdk.com/bds/user/publish_list/?iid=2374555398325096&resolution=1242*2208&os_version=13.5.1&app_name=super&channel=App%20Store&idfa=1ABF0A44-4CBE-4191-B8E6-154836171658&device_platform=iphone&mac_address=02:00:00:00:00:00&vid=86A0335D-BB60-42CC-A461-72D1D67C6DE1&openudid=01942689b4d6f20e58ba3abb334a86fcf32d187c&device_type=iPhone%207%20Plus&idfv=86A0335D-BB60-42CC-A461-72D1D67C6DE1&version_code=3.0.6&ac=WIFI&device_id=2673605010266535&aid=1319&update_version_code=30680&count=20&user_id=6058032285&api_version=1&direction=1"
init_url_4 = "https://is.snssdk.com/bds/user/publish_list/?iid=2374555398325096&resolution=1242*2208&os_version=13.5.1&app_name=super&channel=App%20Store&idfa=1ABF0A44-4CBE-4191-B8E6-154836171658&device_platform=iphone&mac_address=02:00:00:00:00:00&vid=86A0335D-BB60-42CC-A461-72D1D67C6DE1&openudid=01942689b4d6f20e58ba3abb334a86fcf32d187c&device_type=iPhone%207%20Plus&idfv=86A0335D-BB60-42CC-A461-72D1D67C6DE1&version_code=3.0.6&ac=WIFI&device_id=2673605010266535&aid=1319&update_version_code=30680&count=20&user_id=1591688795264663&api_version=1&direction=1"
init_url_5 = ""
init_url_6 = ""
# url
init_url_s = [init_ur_0, init_url_1, init_url_2, init_url_3, init_url_4, init_url_5, init_url_6, ]

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

headers = {
    'Cookie': 'sessionid=158c6ffe4aa1c03f4d8eef9c7487c6a0',
}


def get_download_urls(path_save, init_url, yixiazai, origin_video_download_urls, origin_video_id_s):
    r = requests.get(init_url, headers=headers)
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
        get_download_urls(path_save, init_url, yixiazai, origin_video_download_urls, origin_video_id_s)


def start():
    for index in range(0, len(path_save_s)):
        if index==0:
            continue
        path_save = path_save_s[index]
        print(path_save)
        if path_save == "":
            continue
        path_yixiazai = path_yixiazai_s[index]
        init_url = init_url_s[index]

        origin_video_download_urls = []
        origin_video_id_s = []
        yixiazai = []

        temp = open(path_yixiazai).readlines()
        for item in temp:
            yixiazai.append(item.split("--")[0])

        get_download_urls(path_save, init_url, yixiazai, origin_video_download_urls, origin_video_id_s)

        # 保存
        with open(path_yixiazai, "w+") as file:
            for i in range(0, len(origin_video_id_s)):
                file.writelines(origin_video_id_s[i] + "--" + origin_video_download_urls[i] + "\n")
        print("ok")

start()