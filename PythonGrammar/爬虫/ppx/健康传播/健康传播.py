import os
from urllib.error import HTTPError

import requests
import urllib
from lxml import etree
import os
import json

# (origin)video_download
path = "/Users/chengkun/Downloads/ppx/健康传播/"
files = os.listdir(path)
init_url = "https://is.snssdk.com/bds/user/publish_list/?iid=2937491619330999&resolution=1242*2208&os_version=13.5.1&app_name=super&channel=App%20Store&idfa=6E007FDB-BEAC-493A-B75D-B45F76AEA6BD&device_platform=iphone&mac_address=02:00:00:00:00:00&vid=6248603F-E50C-444D-B928-543FB93C1F8C&openudid=01942689b4d6f20e58ba3abb334a86fcf32d187c&device_type=iPhone%207%20Plus&idfv=6248603F-E50C-444D-B928-543FB93C1F8C&version_code=2.9.8&ac=WIFI&device_id=2673605010266535&aid=1319&update_version_code=29880&count=20&user_id=1591688795264663&api_version=1&direction=1"

headers = {
    'Cookie': 'sessionid=c5000ffd9e68bce0983ef3a7272152af',
}

publish_urls = []
cursor_s = []
origin_video_download_urls = []
origin_video_id_s = []


def get_download_urls(http_url):
    r = requests.get(http_url, headers=headers)
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
            if files.__contains__(str(origin_video_id) + ".mp4"):
                print("已存在：" + origin_video_id)
                continue
            f = urllib.request.urlopen(origin_video_download)
            data = f.read()
            # 存储位置可自定义
            with open(path + str(origin_video_id) + ".mp4", 'wb') as code:
                code.write(data)
        except HTTPError:
            print(origin_video_download)
    cursor = r_json["data"].get("cursor")
    if cursor.get("has_more") == True:
        cursor = cursor.get("loadmore_cursor")
        http_url = init_url.replace("direction=1", "direction=2") + "&cursor=" + str(cursor)
        publish_urls.append(http_url)
        cursor_s.append(cursor)
        get_download_urls(http_url)

get_download_urls(init_url)

with open("id+url.txt", "w") as file:
    for i in range(0, len(origin_video_id_s)):
        file.writelines(origin_video_id_s[i] + "--" + origin_video_download_urls[i] + "\n")

