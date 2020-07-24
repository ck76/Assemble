# coding: utf-8
import os
from pprint import pprint
from wechatarticles.ReadOutfile import Reader
from wechatarticles import ArticlesAPI
from wechatarticles import tools

if __name__ == '__main__':
    username = "xsbdwbd"
    password = "ck276128749"
    official_cookie = "noticeLoginFlag=1; remember_acct=1091480019%40qq.com; ua_id=HhbuYXSWziB9kLdpAAAAACpmtzaG-KlC9HmZ0L6ySDU=; pgv_pvi=8181215232; pgv_pvid=8128021019; RK=TVQADijJOy; ptcz=3c7ce9ad65b6c01822ca80fd5146e3bf505d451d9791f945701ef8a3fb7a676e; tvfe_boss_uuid=6cdf537ba6c7162c; XWINDEXGREY=0; ied_qq=o0276128749; _ga=GA1.2.1971679203.1582105462; o_cookie=276128749; pac_uid=1_276128749; mm_lang=zh_CN; sd_userid=65981589351151899; sd_cookie_crttime=1589351151899; pgg_uid=359380193; pgg_appid=101503919; pgg_openid=14268EF8616B593FD42E2A05DA3F35FB; pgg_access_token=6F33F8D21F3A5CB8B340482F4E4DEF6E; pgg_type=1; pgg_user_type=5; eas_sid=21T5n9A0X5W9a4s9B6L5z5F9S9; ptui_loginuin=1091480019; iip=0; pgv_info=ssid=s1179943512; rewardsn=; wxtokenkey=777; pgv_si=s5242424320; ticket_id=gh_2a5ccbfd8185; cert=8STq3wNZJeblXyA2UHjFeISExr02u1MW; noticeLoginFlag=1; _tucao_userinfo=alBCNXY0TGxLdlhJeVF5aExYNThBeWwwZWo3ajdUbW1DbFlKYzNVT21zV3VSNmlNQWVpR2dVVzJvN1dnME1rMjQvaWRobUJ6SXluREgyQjVGVmJSV1k3aFFqTC9JR0xPVGd4NnNlZFUrYnpWUmoxai9QbWI0T0NENnNobTB2SllrNGFPb2t6SFZtWHMyTFVvMXpFNlFjV2l5aUNNMjdzc2ZCRkMxYXh3TkxwcFhWTmJtWkJEZFliakl6cnRSU1Nv--IoKVyrvt8KQLHPbDJGOXaA%3D%3D; remember_acct=1091480019%40qq.com; uuid=f9bd930fd7e05425a86495f23772c248; bizuin=3225388431; ticket=ec77c90a953f27920750b228cbe9faf5af48dd5a; rand_info=CAESIMY+IfU2TXKpIqRc9ecuqzO4ih/OpSZHW+Xlgllds+Pl; slave_bizuin=3225388431; data_bizuin=3225388431; data_ticket=eoD5wrnrmWCXZQQVmHjKf2FF+y/Ya2zUcAv2Irfhdvtjin1y9xkz6cFJGZ6WpeBq; slave_sid=UFBSMFlRUGVPaTFxaWl4S3BvZzJUSEZiTllzbkF0bm9Lel9uV1c5Tm5LWVd5MVBvSXFFQzJ3VnVUZUZFNW43eG5vYW55aERKN09GdUhqZXhxX0E5dUw4RE5BOGFLcVM5UmJnM2x5VnBxVnpWWkVaMmJZRGdBZWZHdm5VdjA0aDAybUJkcU9ldEFOajZ4eTM4; slave_user=gh_2a5ccbfd8185; xid=494a61cc215ca73d06e599cb246e91d0; openid2ticket_oj4U_wM7sfgAXfofJngIp65Somig=EjV1PQ6t9s2RFY/ZG7WSHGNV50l0aLmOj1x6vbeVCus="
    token = "1066324818"
    appmsg_token = "777"
    wechat_cookie = "devicetype=iMacMacBookPro152OSXOSX10.15.1build(19B88); lang=zh_CN; pass_ticket=fgd4PG3TNgKsBzgUwWgb+lvtgwr0ylHHBLmavTAuCJsETW6/99x2OIWtOQtQHR56; rewardsn=; version=12040110; wap_sid2=CJGU86oHElxPaXdQSjJGOTZhWWRlenVnTzd2aUhzNjhONzB1NUJUeGJVYU1MTjBNYVd2ZjZENTJ4MUZ5NF91RDhrUWZRSzN0dXg4OWxjbkNHRlFnWkZOdnJrNU40eTBFQUFBfjDsubf4BTgNQAE=; wxtokenkey=777; wxuin=1969015313; pgv_pvid=3775375840; pgv_pvi=5127429120"

    nickname = "小树不倒我不倒啊"

    # 手动输入所有参数
    test = ArticlesAPI(official_cookie=official_cookie,
                       token=token,
                       appmsg_token=appmsg_token,
                       wechat_cookie=wechat_cookie)

    # # 输入账号密码，自动登录公众号，手动输入appmsg_token和wechat_cookie
    # test = ArticlesAPI(username=username,
    #                    password=password,
    #                    appmsg_token=appmsg_token,
    #                    wechat_cookie=wechat_cookie)
    #
    # # 手动输入official_cookie和token, 自动获取appmsg_token和wechat_cookie
    # test = ArticlesAPI(official_cookie=official_cookie,
    #                    token=token,
    #                    outfile="outfile")
    #
    # # 输入帐号密码，自动登陆公众号, 自动获取appmsg_token和wechat_cookie
    # test = ArticlesAPI(username=username, password=password, outfile="outfile")

    # 自定义爬取，每次爬取5篇以上
    print("0")
    data = test.complete_info(nickname=nickname, begin="6",count=10)
    print("1")
    print(data.__len__())
    pprint(data)

    # 自定义从某部分开始爬取，持续爬取，直至爬取失败为止，一次性最多爬取40篇（功能未测试，欢迎尝试）
    datas = test.continue_info(nickname=nickname, begin="0")

    tools.save_json("test.json", data)