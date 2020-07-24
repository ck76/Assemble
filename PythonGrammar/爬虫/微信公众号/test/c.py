from wechatarticles import ArticlesAPI
from wechatarticles import ArticlesUrls

# # 实例化爬取对象
# # 账号密码自动获取cookie和token
# test = ArticlesUrls(username="xsbdwbd", password="ck276128749")
# # 手动输入账号密码
# test = ArticlesUrls(cookie="noticeLoginFlag=1; remember_acct=1091480019%40qq.com; ua_id=HhbuYXSWziB9kLdpAAAAACpmtzaG-KlC9HmZ0L6ySDU=; pgv_pvi=8181215232; pgv_pvid=8128021019; RK=TVQADijJOy; ptcz=3c7ce9ad65b6c01822ca80fd5146e3bf505d451d9791f945701ef8a3fb7a676e; tvfe_boss_uuid=6cdf537ba6c7162c; XWINDEXGREY=0; ied_qq=o0276128749; _ga=GA1.2.1971679203.1582105462; o_cookie=276128749; pac_uid=1_276128749; mm_lang=zh_CN; sd_userid=65981589351151899; sd_cookie_crttime=1589351151899; pgg_uid=359380193; pgg_appid=101503919; pgg_openid=14268EF8616B593FD42E2A05DA3F35FB; pgg_access_token=6F33F8D21F3A5CB8B340482F4E4DEF6E; pgg_type=1; pgg_user_type=5; eas_sid=21T5n9A0X5W9a4s9B6L5z5F9S9; ptui_loginuin=1091480019; iip=0; pgv_info=ssid=s1179943512; rewardsn=; wxtokenkey=777; pgv_si=s5242424320; ticket_id=gh_2a5ccbfd8185; cert=8STq3wNZJeblXyA2UHjFeISExr02u1MW; noticeLoginFlag=1; _tucao_userinfo=alBCNXY0TGxLdlhJeVF5aExYNThBeWwwZWo3ajdUbW1DbFlKYzNVT21zV3VSNmlNQWVpR2dVVzJvN1dnME1rMjQvaWRobUJ6SXluREgyQjVGVmJSV1k3aFFqTC9JR0xPVGd4NnNlZFUrYnpWUmoxai9QbWI0T0NENnNobTB2SllrNGFPb2t6SFZtWHMyTFVvMXpFNlFjV2l5aUNNMjdzc2ZCRkMxYXh3TkxwcFhWTmJtWkJEZFliakl6cnRSU1Nv--IoKVyrvt8KQLHPbDJGOXaA%3D%3D; remember_acct=1091480019%40qq.com; uuid=f9bd930fd7e05425a86495f23772c248; bizuin=3225388431; ticket=ec77c90a953f27920750b228cbe9faf5af48dd5a; rand_info=CAESIMY+IfU2TXKpIqRc9ecuqzO4ih/OpSZHW+Xlgllds+Pl; slave_bizuin=3225388431; data_bizuin=3225388431; data_ticket=eoD5wrnrmWCXZQQVmHjKf2FF+y/Ya2zUcAv2Irfhdvtjin1y9xkz6cFJGZ6WpeBq; slave_sid=UFBSMFlRUGVPaTFxaWl4S3BvZzJUSEZiTllzbkF0bm9Lel9uV1c5Tm5LWVd5MVBvSXFFQzJ3VnVUZUZFNW43eG5vYW55aERKN09GdUhqZXhxX0E5dUw4RE5BOGFLcVM5UmJnM2x5VnBxVnpWWkVaMmJZRGdBZWZHdm5VdjA0aDAybUJkcU9ldEFOajZ4eTM4; slave_user=gh_2a5ccbfd8185; xid=494a61cc215ca73d06e599cb246e91d0; openid2ticket_oj4U_wM7sfgAXfofJngIp65Somig=EjV1PQ6t9s2RFY/ZG7WSHGNV50l0aLmOj1x6vbeVCus=", token="1066324818")
#
# # 输入公众号名称，获取公众号文章总数
# articles_sum = test.articles_nums("奥丁读书小站")
# print(articles_sum)
# # 输入公众号名称，获取公众号部分文章信息, 每次最大返回数为5个
# articles_data = test.articles("奥丁读书小站", begin="0", count="5")
# print(articles_data)
# # 输入公众号名称，获取公众号的一些信息
# officical_info = test.official_info("奥丁读书小站")
# print(officical_info)
# # 输入公众号名称，输入关键词，获取公众号相关文章信息, 每次最大返回数为5个
# # articles_data_query = test.articles("奥丁读书小站", query=query, begin="0", count="5")
# # 输入公众号名称，输入关键词，获取公众号相关文章总数
# # articles_sum_query = test.articles_nums(nickname, query=query)
#
# # 支持自动获取appmsg_token和cookie
# # appmsg_token, cookie = Reader().contral(outfile)
#
# # 实例化爬取对象
# # # 账号密码自动获取cookie和token
# # test = ArticlesInfo(appmsg_token=appmsg_token, cookie=wechat_cookie)
# # # 获取文章所有的评论信息(无需appmsg_token和cookie)
# # comments = test.comments(link)
# # # 获取文章阅读数在看点赞数
# # read_num, like_num, old_like_num = test.read_like_nums(link)
#
# art = ArticlesAPI(username="xsbdwbd", password="ck276128749",
#                   official_cookie="ua_id=HhbuYXSWziB9kLdpAAAAACpmtzaG-KlC9HmZ0L6ySDU=; pgv_pvi=8181215232; pgv_pvid=8128021019; RK=TVQADijJOy; ptcz=3c7ce9ad65b6c01822ca80fd5146e3bf505d451d9791f945701ef8a3fb7a676e; tvfe_boss_uuid=6cdf537ba6c7162c; XWINDEXGREY=0; ied_qq=o0276128749; _ga=GA1.2.1971679203.1582105462; o_cookie=276128749; pac_uid=1_276128749; mm_lang=zh_CN; sd_userid=65981589351151899; sd_cookie_crttime=1589351151899; pgg_uid=359380193; pgg_appid=101503919; pgg_openid=14268EF8616B593FD42E2A05DA3F35FB; pgg_access_token=6F33F8D21F3A5CB8B340482F4E4DEF6E; pgg_type=1; pgg_user_type=5; eas_sid=21T5n9A0X5W9a4s9B6L5z5F9S9; ptui_loginuin=1091480019; iip=0; pgv_info=ssid=s1179943512; rewardsn=; wxtokenkey=777; pgv_si=s5242424320; ticket_id=gh_2a5ccbfd8185; cert=8STq3wNZJeblXyA2UHjFeISExr02u1MW; noticeLoginFlag=1; _tucao_userinfo=alBCNXY0TGxLdlhJeVF5aExYNThBeWwwZWo3ajdUbW1DbFlKYzNVT21zV3VSNmlNQWVpR2dVVzJvN1dnME1rMjQvaWRobUJ6SXluREgyQjVGVmJSV1k3aFFqTC9JR0xPVGd4NnNlZFUrYnpWUmoxai9QbWI0T0NENnNobTB2SllrNGFPb2t6SFZtWHMyTFVvMXpFNlFjV2l5aUNNMjdzc2ZCRkMxYXh3TkxwcFhWTmJtWkJEZFliakl6cnRSU1Nv--IoKVyrvt8KQLHPbDJGOXaA%3D%3D; remember_acct=1091480019%40qq.com; uuid=f9bd930fd7e05425a86495f23772c248; bizuin=3225388431; ticket=ec77c90a953f27920750b228cbe9faf5af48dd5a; rand_info=CAESIMY+IfU2TXKpIqRc9ecuqzO4ih/OpSZHW+Xlgllds+Pl; slave_bizuin=3225388431; data_bizuin=3225388431; data_ticket=eoD5wrnrmWCXZQQVmHjKf2FF+y/Ya2zUcAv2Irfhdvtjin1y9xkz6cFJGZ6WpeBq; slave_sid=UFBSMFlRUGVPaTFxaWl4S3BvZzJUSEZiTllzbkF0bm9Lel9uV1c5Tm5LWVd5MVBvSXFFQzJ3VnVUZUZFNW43eG5vYW55aERKN09GdUhqZXhxX0E5dUw4RE5BOGFLcVM5UmJnM2x5VnBxVnpWWkVaMmJZRGdBZWZHdm5VdjA0aDAybUJkcU9ldEFOajZ4eTM4; slave_user=gh_2a5ccbfd8185; xid=494a61cc215ca73d06e599cb246e91d0; openid2ticket_oj4U_wM7sfgAXfofJngIp65Somig=EjV1PQ6t9s2RFY/ZG7WSHGNV50l0aLmOj1x6vbeVCus=",
#                   token="1066324818",
#                   appmsg_token=None,
#                   wechat_cookie=None,
#                   outfile=None)
#
# art.complete_info(nickname="奥丁读书小站")
aurls=ArticlesUrls(username="xsbdwbd", password="ck276128749",
             cookie="ua_id=HhbuYXSWziB9kLdpAAAAACpmtzaG-KlC9HmZ0L6ySDU=; pgv_pvi=8181215232; pgv_pvid=8128021019; RK=TVQADijJOy; ptcz=3c7ce9ad65b6c01822ca80fd5146e3bf505d451d9791f945701ef8a3fb7a676e; tvfe_boss_uuid=6cdf537ba6c7162c; XWINDEXGREY=0; ied_qq=o0276128749; _ga=GA1.2.1971679203.1582105462; o_cookie=276128749; pac_uid=1_276128749; mm_lang=zh_CN; sd_userid=65981589351151899; sd_cookie_crttime=1589351151899; pgg_uid=359380193; pgg_appid=101503919; pgg_openid=14268EF8616B593FD42E2A05DA3F35FB; pgg_access_token=6F33F8D21F3A5CB8B340482F4E4DEF6E; pgg_type=1; pgg_user_type=5; eas_sid=21T5n9A0X5W9a4s9B6L5z5F9S9; ptui_loginuin=1091480019; iip=0; pgv_info=ssid=s1179943512; rewardsn=; wxtokenkey=777; pgv_si=s5242424320; ticket_id=gh_2a5ccbfd8185; cert=8STq3wNZJeblXyA2UHjFeISExr02u1MW; noticeLoginFlag=1; _tucao_userinfo=alBCNXY0TGxLdlhJeVF5aExYNThBeWwwZWo3ajdUbW1DbFlKYzNVT21zV3VSNmlNQWVpR2dVVzJvN1dnME1rMjQvaWRobUJ6SXluREgyQjVGVmJSV1k3aFFqTC9JR0xPVGd4NnNlZFUrYnpWUmoxai9QbWI0T0NENnNobTB2SllrNGFPb2t6SFZtWHMyTFVvMXpFNlFjV2l5aUNNMjdzc2ZCRkMxYXh3TkxwcFhWTmJtWkJEZFliakl6cnRSU1Nv--IoKVyrvt8KQLHPbDJGOXaA%3D%3D; remember_acct=1091480019%40qq.com; uuid=f9bd930fd7e05425a86495f23772c248; bizuin=3225388431; ticket=ec77c90a953f27920750b228cbe9faf5af48dd5a; rand_info=CAESIMY+IfU2TXKpIqRc9ecuqzO4ih/OpSZHW+Xlgllds+Pl; slave_bizuin=3225388431; data_bizuin=3225388431; data_ticket=eoD5wrnrmWCXZQQVmHjKf2FF+y/Ya2zUcAv2Irfhdvtjin1y9xkz6cFJGZ6WpeBq; slave_sid=UFBSMFlRUGVPaTFxaWl4S3BvZzJUSEZiTllzbkF0bm9Lel9uV1c5Tm5LWVd5MVBvSXFFQzJ3VnVUZUZFNW43eG5vYW55aERKN09GdUhqZXhxX0E5dUw4RE5BOGFLcVM5UmJnM2x5VnBxVnpWWkVaMmJZRGdBZWZHdm5VdjA0aDAybUJkcU9ldEFOajZ4eTM4; slave_user=gh_2a5ccbfd8185; xid=494a61cc215ca73d06e599cb246e91d0; openid2ticket_oj4U_wM7sfgAXfofJngIp65Somig=EjV1PQ6t9s2RFY/ZG7WSHGNV50l0aLmOj1x6vbeVCus=",
             token="1066324818")
aurls.articles(nickname="奥丁读书小站")