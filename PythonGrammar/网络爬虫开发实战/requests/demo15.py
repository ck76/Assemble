import requests

headers = {
    'Cookie': 'zap=43fdc0b0-ee16-41b4-b38e-0ee4e0328598; d_c0="ABCnh6DaOBCPTjSvKVQ2V87tg8ZS30HFhpw=|1571473315"; __utmv=51854390.100-1|2=registration_date=20150930=1^3=entry_date=20150930=1; __utmz=51854390.1580229047.5.5.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _ga=GA1.2.270544613.1574337777; __utma=51854390.270544613.1574337777.1580229047.1585018012.6; tst=f; z_c0="2|1:0|10:1587894958|4:z_c0|92:Mi4xODVBa0FnQUFBQUFBRUtlSG9ObzRFQ1lBQUFCZ0FsVk5ycWlTWHdEZTZwTzN1YnZHZVhmaXEwdkpuOWExUi1uSVdn|9e55d3304b4fc0e6857bbfe1386f6541d7c8478f93ad5972923dbd444a046356"; _xsrf=yHDthuoT6ZGvdnAgRhNM5sL8CZncUPG1; q_c1=b339ecdb921b42f98510035871da0772|1590382651000|1572172738000; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1592665264,1592701666,1592704649,1592706324; _gid=GA1.2.460838725.1592877050; SESSIONID=OJdPBAMCjME66xN9xKsuYiVhnch076CjMLwIpH8eGP9; JOID=VlwRC0OESNPcsE6qI4hkxWOAj9EyywK7jP4P52ziBZbmhjrkGlglLo68TqYvSekihsQ91U6oePtemrO2r8dAo0Y=; osd=U1EcB06BRd7QvUunLoRpwG6Ng9w3xg-3gfsC6mDvAJvrijfhF1UpI4uxQ6oiTOQvisk42EOkdf5Tl7-7qspNr0s=; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1592877769; _gat_gtag_UA_149949619_1=1; KLBRSID=e42bab774ac0012482937540873c03cf|1592877771|1592877048' ,
    'Host': 'www.zhihu.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
}
r = requests.get('https://www.zhihu.com', headers=headers)
print(r.text)