import re

import requests
from urllib.parse import urlparse
from urllib.parse import parse_qs

from lxml import etree
# <ul class="ul_Address"><script type="text/javascript" src="/inc/downLoad.asp?Address=cyjsjdmw%2Epdf&TypeID=1&SoftLinkID=16144&SoftID=524943"></script></ul>
r=requests.get("http://www.j9p.com/inc/downLoad.asp?Address=tetjsxnx%2Ezip&TypeID=1&SoftLinkID=15732&SoftID=524538")
print(r.text)

result=urlparse("inc/downLoad.asp?Address=tetjsxnx%2Ezip&TypeID=1&SoftLinkID=15732&SoftID=524538")
print(result)
print(parse_qs(result.query).get("Address"))
# print(type(r.text))
# url = re.compile(r'^http.*?zip$').findall(str(r.text))
# print(url)
#
# ck="""
# http:dsadas.zip
# document.write("<li class=\"address_like\"><a href='http://jxz1.j9p.com/pc/tetjsxnx.zip' target='_blank' onclick=\"softCount(524538,15732)\">广东电信下载</a></li>");
# """
# print(re.compile(r'^http.*?zip$').findall(ck))

error_url="http://www.j9p.com//down/525516.html"

html="""

<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=gb2312"/>
<title>数据中台：让数据用起来pdf下载-精品下载</title>
<meta name="keywords" content="数据中台让数据用起来,小数据之美">
<meta name="description" content="数据中台：让数据用起来pdf是一本对数据中台进行详细概述的书籍，在书中所有的作者都是资深的专家，大家可以通过这本书来了解到数据中台，非常实用！" />
<link href="/css/reset.css" rel="stylesheet" media="screen">
<link href="/css/detail2019.css" rel="stylesheet">
<script src="/js/jquery-3.4.1.min.js"></script>
<script src="/js/fy-all.min.js"></script>
<script src="/js/swiper.min.js"></script>
<script> var _pageinfo = { id: "525516", path: "down"}</script>
</head>
<body>
<div class="g-top">
<p> <span class="left">精品下载站：打造最安全最新的免费软件下载站!</span> <span class="right"><a href="http://www.j9p.com/class/">全站导航</a><a href="http://www.j9p.com/Other/0_1.html">最近更新</a></span> </p>
</div>
<div class="g-header">
<div class="m-logo"> <a href="/"><img src="/images/logo.png"></a> </div>
<div class="m-search">
<div class="searchform">
<form style="padding: 0px; margin-top:0px;" name="topForm" class="searchbox" id="topForm" action="/search.asp">
<input type="text" class="keyword_input" id="keyword" name="keyword" placeholder="请输入关键词">
<input type="submit" class="schbtn" value="搜 索">
<input type="hidden" value="" id="searchType" name="searchType">
</form>
</div>
<p><b>热门搜索：</b>
<a href="/down/524098.html">生活需要仪式感2PDF</a>
<a href="/down/521559.html">GPS卫星导航基础pdf</a>
<a href="/down/521493.html">好的焦虑pdf</a>
<a href="/down/521488.html">有效资产管理pdf下载</a>
<a href="/down/521417.html">超级运营术PDF</a>
</p>
</div>
</div>
<div class="g-nav">
<ul>
<li><a href="http://www.j9p.com/">首页</a></li>
<li><a href="http://www.j9p.com/doc.html">素材下载</a></li>
<li class="hover"><a href="http://www.j9p.com/index_pc.html">电脑软件</a></li>
<li><a href="http://www.j9p.com/class/r_12_1.html">安卓应用</a></li>
<li><a href="http://www.j9p.com/class/r_13_1.html">安卓游戏</a></li>
<li><a href="http://www.j9p.com/class/r_14_1.html">苹果应用</a></li>
<li><a href="http://www.j9p.com/class/r_15_1.html">苹果游戏</a></li>
<li><a href="http://www.j9p.com/article/">文章</a></li>
</ul>
</div>
<div class="g-softinfo-nav"><a href="/">首页</a> → <a href="/class/r_16_1.html">pdf文件</a> → <a href="/class/182_1.html">互联网/科技</a> → 数据中台：让数据用起来pdf下载 </div>
<div class="g-softinfo">
<div class="g-softinfo-box">
<div class="img"><img src="http://pic.j9p.com/up/2020-5/2020513834416303.png"></div>
<div class="info">
<h1>数据中台：让数据用起来pdf下载</h1>
<ul>
<li>授权方式：免费软件</li>
<li>软件类型：国产软件</li>
<li>软件来源：暂无</li>
<li>更新时间：2020-05-13</li>
<li>官方网址：暂无</li>
<li>软件大小：18.5M</li>
<li>推荐星级：<img src="/images/3star.gif"></li>
<li>运行环境：WinAll, 64位, 32位</li>
</ul>
</div>
<div class="features">
<div id="vote" class="m-vote">
<div id="isgood" class="vote_bar"><b></b><span><img src="/images/isgoodd.png" style="width:50%" alt="好玩"/></span><i>10</i></div>
<div id="isbad" class="vote_bar"><b></b> <span><img src="/images/isbadd.png" style="width:50%" alt="坑爹"/></span><i>10</i></div>
</div>
<p class="localdown">
<a href="../down.asp?id=525516" title="右击另存为或点击跳转到下载地址">
<b>本地下载</b>
<em>文件大小：18.5M</em>
</a>
</p>
<p class="speeddown">
<a href="http://www.uzzf.com/soft/580760.html" title="迅雷9精简版不限速破解版">
<b>高速下载</b>
<em>需优先下载高速下载器</em>
</a>
</p>
</div>
</div>
</div>
<dl class="g-softcontent">
<dt class="g-softcontent-left">
<p class="m-tabnav">
<span class="hover">软件介绍</span>
<span>软件截图</span>
<span>相关下载</span>
<span>相关文章</span>
<span>点击评论</span>
</p>
<p class="m-tags"><span>软件标签：</span><a href='/tags/%CA%FD%BE%DD%D6%D0%CC%A8%C8%C3%CA%FD%BE%DD%D3%C3%C6%F0%C0%B4.html' target='_blank'> 数据中台让数据用起来</a><a href='/tags/%D0%A1%CA%FD%BE%DD%D6%AE%C3%C0.html' target='_blank'> 小数据之美</a></p>
<div id="content" class="m-content" data-ride="mfolder" data-spread-text="展开" data-fold-text="收起" data-sub-height="200">
<p></p>
<p><strong>数据中台：让数据用起来pdf</strong>是一本对数据中台进行详细概述的书籍，在书中所有的作者都是资深的专家，大家可以通过这本书来了解到数据中台，非常实用！</p><p><img src="http://pic.j9p.com/up/2020-5/15893304355975401.png" title="数据中台：让数据用起来pdf下载" alt="数据中台：让数据用起来pdf下载"/></p><h3>电子书内容提要</h3><p>这是一部系统讲解数据中台建设、管理与运营的著作，旨在帮助企业将数据转化为生产力，顺利实现数字化转型。</p><p>本书由国内数据中台领域的领先企业数澜科技官方出品，几位联合创始人亲自执笔，7位作者都是资深的数据人，大部分作者来自原阿里巴巴数据中台团队。他们结合过去帮助百余家各行业头部企业建设数据中台的经验，系统总结了一套可落地的数据中台建设方法论。本书得到了包括阿里巴巴集团联合创始人在内的多位行业专家的高度评价和推荐。</p><p>全书一共11章，从建设、管理、运营、安全等维度全方位地讲解了数据中台。</p><p>第1~2章全面介绍了数据中台产生的背景、发展阶段、企业应该具备的3个认知，以及什么是数据中台、数据中台的4个核心能力、数据中台的业务价值与技术价值等；</p><p>第3~4章详细讲解了数据中台的架构设计、建设方法论，以及企业建设数据中台的成熟度评估和应用场景分析；</p><p>第5~9章深入地讲解了数据汇聚与联通、数据开发、数据体系建设、数据资产管理、数据服务体系建设等数据中台的核心模块，以及如何从0到1实现一个数据中台；</p><p>第10~11章详细地讲解了数据中台的管理、运营和安全保障。</p><h3>书籍作者资料</h3><p><strong>数澜科技</strong></p><p>数澜科技成立于2016年6月，秉持“让企业的数据用起来”的使命，致力于成为客户信赖的数据应用基础设施供应商。2019年初，跻身“杭州准独角兽企业”榜。</p><p>自成立之日起，数澜团队即坚持以“数据中台”作为核心战略构建和培养团队，建成以数据科学家、数据产品专家、数据咨询专家及数据可视化专家为核心的数据科技研发团队，核心成员来自阿里、华为等企业，拥有大数据业务和技术多年实战经验，是国内早一批大数据服务创新实践者。</p><p>目前，数澜已为万科、方太、兴业银行、百果园、中信云网、时尚集团、温州检察院、喜茶、视源股份等多家行业头部企业和政府客户，提供了数据中台建设和数据资产开发服务，并基于数栖帮助企业持续挖掘数据资产，赋能业务创新。</p><p>数澜官网：www.dtwave.com</p><p>微信公众号：dtwave0620</p><p><strong>付登坡（花名：天湛）</strong></p><p>资深大数据专家，数澜科技联合创始人&amp;地产事业部总经理</p><p>有10余年?数据领域从业经验，擅长数据建模、海量数据产品架构设计与实现。原阿?巴巴集团?数据专家，曾在阿里集团负责消费者数据标签体系、DMP平台等大数据项?设计与实施。2015年以创始人身份组建阿?巴巴集团的“11维数据创新工作室”，探索数据创新与数据商业化。</p><p>2016年6?离职，联合创办数澜科技，在数澜科技先后负责技术部、咨询服务部、地产事业部。</p><p><strong>江敏（花名：江敏）</strong></p><p>资深大数据专家，数澜科技联合创始人&amp;CTO</p><p>有10年大数据平台规划、数据安全交换使用、数据应用场景建设方面的实践经验。曾任职于阿里数据平台事业部、阿里云数据事业部，负责阿里数据能力及平台的行业客户赋能，ID-Mapping体系能力构建及服务化的核心参与者，并打造行业的数据共享交换，数据交易模式早期探索者。</p><p>数澜科技联合创始人，负责管理公司产品技术团队，为客户输出构建和经营数据中台的能力，基于数据中台建设的实践经验，带领团队打造一站式数据应用基础设施-数栖，并完成实施多家行业龙头客户基于数栖的数据中台建设。</p><p><strong>任寅姿（花名：影姿）</strong></p><p>资深数据产品专家，数澜科技创新事业部总经理</p><p>曾任阿里巴巴数据产品专家、数据创新梧桐工作室负责人等。对大数据资产设计、资产服务、资产应用在实践的基础上形成了一套完整的数据标签类目体系方法论；擅长对各种复杂业务场景进行需求拆解、数据抽象和数据应用建模，关注于采用大数据方法切实解决场景痛点提升业务效率。</p><p><strong>孙少忆（花名：守正）</strong></p><p>资深数字化转型咨询专家，数澜科技战略副总裁</p><p>20年企业信息化工作经验,积累信息化内部运营、解决方案销售及交付等领域实践经验。拥有MBCI、CISSP-ISSMP、CGEIT、COBIT5、ITILExpert、P3O等国际专业资质证书。曾任职华为ICT规划咨询部，面向企业、政府提供“以数据为核心，聚焦业务场景和价值”的流程信息化与数字化转型规划和落地咨询业务。</p><p><strong>武凯（花名：行竹）</strong></p><p>资深数据产品专家，数澜科技COO</p><p>有10余年数据产品经验，曾任阿里巴巴集团数据平台产品与运营部负责人，是营销、零售和医疗健康等领域数据应用的探索实践者，专注于企业大数据资产化及应用增值。</p><p><strong>沈金（花名：铁平）</strong></p><p>资深数据业务架构专家，数澜科技解决方案总监</p><p>10余年数据行业经验，擅长业务架构、数据架构、技术架构的规划和落地实施。曾在阿?巴巴担任DBA，后参与阿里数据中台建设，拥有用户识别、标签设计、动态数据组织多个发明专利。</p><p>2017年加入数澜科技，负责解决方案团队，推动数据中台在零售、地产、金融、集团等客户案例落地。</p><p><strong>蔣珍波（花名：乐天）</strong></p><p>大数据咨询专家，数澜科技高级咨询专家</p><p>15年信息化和大数据行业从业经验，具备广阔的知识面，丰富的咨询经验，擅长创造性地为客户提供解决方案，尤其擅长数据治理方面的咨询规划和产品设计，服务过数十家政府和大中型企业客户。</p><h3>章节目录内容</h3><p>第1章 数据中台：信息化的下一站</p><p>第2章 什么是数据中台</p><p>第3章 数据中台建设与架构</p><p>第4章 数据中台建设的评估与选择</p><p>第5章 数据汇聚联通：打破企业数据孤岛</p><p>第6章 数据开发：数据价值提炼工厂</p><p>第7章 数据体系建设</p><p>第8章 数据资产管理</p><p>第9章 数据服务体系建设</p><p>第10章 数据中台运营机制</p><p>第11章 数据安全管理</p>
</div>
<div class="f-rolling clearfix" id="fy-rolling" data-ride="rolling" data-stretch="false" data-auto="true" data-num="6">
<div class="cbox m-jietu"><h3>数据中台：让数据用起来pdf下载截图</h3></div>
<div class="swiper-container">
<div class="swiper-wrapper">
<div class="swiper-slide"><img src="http://pic.j9p.com/up/2020-5/202051383449653750.png" alt="数据中台：让数据用起来pdf下载截图0"/></div>
<div class="swiper-slide"><img src="http://pic.j9p.com/up/2020-5/202051383454774870.png" alt="数据中台：让数据用起来pdf下载截图1"/></div>
</div>
<div class="swiper-button-prev"></div>
<div class="swiper-button-next"></div>
</div>
</div>
<div class="m-related">
<p class="title"><span>相关下载</span></p>
<div class="screenshots-ul clearfix">
<a href="/down/525501.html" target="_blank" data-language="中文" data-size="5.2M" data-rank="2">
<img src="http://pic.j9p.com/up/2020-5/20205111337155799.jpg" alt="淘宝天猫SEO从入门到精通pdf下载" /><strong>淘宝天猫SEO从入门到精通pdf下载</strong>
</a>
<a href="/down/525409.html" target="_blank" data-language="中文" data-size="2.9M" data-rank="3">
<img src="http://pic.j9p.com/up/2020-5/202059101153539.png" alt="燃点：正在发生的创业史pdf下载" /><strong>燃点：正在发生的创业史pdf下载</strong>
</a>
<a href="/down/525405.html" target="_blank" data-language="中文" data-size="2.0M" data-rank="2">
<img src="http://pic.j9p.com/up/2020-5/2020599353836.png" alt="智能与智慧PDF电子书" /><strong>智能与智慧PDF电子书</strong>
</a>
<a href="/down/525354.html" target="_blank" data-language="中文" data-size="7.4M" data-rank="3">
<img src="http://pic.j9p.com/up/2020-5/2020581358354797.png" alt="大型网站服务器容量规划pdf下载" /><strong>大型网站服务器容量规划pdf下载</strong>
</a>
<a href="/down/525346.html" target="_blank" data-language="中文" data-size="1.5M" data-rank="3">
<img src="http://pic.j9p.com/up/2020-5/202058113487926.png" alt="大教堂与集市pdf最新版" /><strong>大教堂与集市pdf最新版</strong>
</a>
<a href="/down/525332.html" target="_blank" data-language="中文" data-size="7.3M" data-rank="3">
<img src="http://pic.j9p.com/up/2020-5/202058943544707.png" alt="人人都该懂的互联网思维PDF电子书" /><strong>人人都该懂的互联网思维PDF电子书</strong>
</a>
<a href="/down/525299.html" target="_blank" data-language="中文" data-size="3.1M" data-rank="2">
<img src="http://pic.j9p.com/up/2020-5/202057162293750.jpg" alt="工具，还是武器？PDF电子书下载" /><strong>工具，还是武器？PDF电子书下载</strong>
</a>
<a href="/down/525266.html" target="_blank" data-language="中文" data-size="2.7M" data-rank="2">
<img src="http://pic.j9p.com/up/2020-5/2020571012488733.jpg" alt="孙正义传：打造300年企业帝国的野心电子书" /><strong>孙正义传：打造300年企业帝国的野心电子书</strong>
</a>
<a href="/down/525139.html" target="_blank" data-language="中文" data-size="5.4M" data-rank="2">
<img src="http://pic.j9p.com/up/2020-4/20204291124278332.png" alt="轻营销：小预算玩转大市场(第3版)电子书" /><strong>轻营销：小预算玩转大市场(第3版)电子书</strong>
</a>
<a href="/down/525039.html" target="_blank" data-language="中文" data-size="4.5M" data-rank="2">
<img src="http://pic.j9p.com/up/2020-4/20204271735143561.png" alt="成为数据分析师pdf" /><strong>成为数据分析师pdf</strong>
</a>
<a href="/down/525020.html" target="_blank" data-language="中文" data-size="1.7M" data-rank="2">
<img src="http://pic.j9p.com/up/2020-4/2020427156315908.png" alt="18个未来进行时pdf" /><strong>18个未来进行时pdf</strong>
</a>
<a href="/down/524984.html" target="_blank" data-language="中文" data-size="4.3M" data-rank="2">
<img src="http://pic.j9p.com/up/2020-4/20204261956181649.jpg" alt="大数据营销：定位客户PDF电子版" /><strong>大数据营销：定位客户PDF电子版</strong>
</a>
<a href="/down/524976.html" target="_blank" data-language="中文" data-size="18.2M" data-rank="3">
<img src="http://pic.j9p.com/up/2020-4/20204261749501373.png" alt="崛起的超级智能pdf" /><strong>崛起的超级智能pdf</strong>
</a>
<a href="/down/524954.html" target="_blank" data-language="中文" data-size="2.9M" data-rank="3">
<img src="http://pic.j9p.com/up/2020-4/20204261429567465.png" alt="区块链金融应用发展白皮书PDF电子书完整版" /><strong>区块链金融应用发展白皮书PDF电子书完整版</strong>
</a>
<a href="/down/524951.html" target="_blank" data-language="中文" data-size="6.8M" data-rank="2">
<img src="http://pic.j9p.com/up/2020-4/2020426146491360.png" alt="社群营销与运营pdf免费下载" /><strong>社群营销与运营pdf免费下载</strong>
</a>
<a href="/down/524949.html" target="_blank" data-language="中文" data-size="1.6M" data-rank="2">
<img src="http://pic.j9p.com/up/2020-4/2020426135037067.png" alt="人人时代：无组织的组织力量pdf下载" /><strong>人人时代：无组织的组织力量pdf下载</strong>
</a>
<a href="/down/524943.html" target="_blank" data-language="中文" data-size="5.6M" data-rank="2">
<img src="http://pic.j9p.com/up/2020-4/2020426113733512.png" alt="穿越计算机的迷雾pdf免费下载" /><strong>穿越计算机的迷雾pdf免费下载</strong>
</a>
<a href="/down/524939.html" target="_blank" data-language="中文" data-size="3.8M" data-rank="2">
<img src="http://pic.j9p.com/up/2020-4/2020426112172541.jpg" alt="明智转向：数字时代的转型思维和增长模式电子书" /><strong>明智转向：数字时代的转型思维和增长模式电子书</strong>
</a>
<a href="/down/524915.html" target="_blank" data-language="中文" data-size="9.7M" data-rank="2">
<img src="http://pic.j9p.com/up/2020-4/20204251721428886.jpg" alt="一本书读懂区块链pdf下载" /><strong>一本书读懂区块链pdf下载</strong>
</a>
<a href="/down/524913.html" target="_blank" data-language="中文" data-size="1.2M" data-rank="2">
<img src="http://pic.j9p.com/up/2020-4/2020425177412219.jpg" alt="删除：大数据取舍之道pdf下载" /><strong>删除：大数据取舍之道pdf下载</strong>
</a>
<a href="/down/524907.html" target="_blank" data-language="中文" data-size="8.7M" data-rank="2">
<img src="http://pic.j9p.com/up/2020-4/20204251412266074.png" alt="实战Java高并发程序设计pdf下载" /><strong>实战Java高并发程序设计pdf下载</strong>
</a>
</div>
</div>
<div class="m-article">
<p class="title"><span>相关文章</span></p>
<ul>
</ul>
</div>
<div class="m-downaddress">
<p class="title"><span>下载地址</span></p>
<h3> 数据中台：让数据用起来pdf下载</h3>
<ul class="ul_Address"><script type="text/javascript" src="/inc/downLoad.asp?Address=sjztdzs%2Epdf&TypeID=1&SoftLinkID=16723&SoftID=525516"></script></ul>
</div>
<div class="m-pl">
<p class="title"><span>点击评论</span></p>
<div id="comment_list">
<div id="comment_0">
<div class="h2"><span>热门评论</span></div>
<dl>
</dl>
</div>
<div id="comment_1">
<div class="h2"><span>最新评论</span></div>
<dl>
</dl>
</div>
<div id="s_comment">
<form action="" id="zt_ly">
<div class="h2"><span>发表评论</span> <a href="/comment_525516_0.html">查看所有评论(<i>0</i>)</a></div>
<div class="nick_name"><b>昵称: </b>
<input name="UserName" type="text" id="UserName" value="精品下载网网友" />
<input name="ly_id" type="hidden" id="ly_id" value="525516" />
<input name="CommentTpye" type="hidden" id="ztid" value="0" />
</div>
<div class="comment_faces">
<b>表情:</b>
<img src="http://www.j9p.com/images/1.gif" alt="高兴" width="24" height="24" data-face-id="1"/>
<img src="http://www.j9p.com/images/2.gif" alt="可" width="24" height="24" data-face-id="2"/>
<img src="http://www.j9p.com/images/3.gif" alt="汗" width="24" height="24" data-face-id="3"/>
<img src="http://www.j9p.com/images/4.gif" alt="我不要" width="24" height="24" data-face-id="4"/>
<img src="http://www.j9p.com/images/5.gif" alt="害羞" width="24" height="24" data-face-id="5"/>
<img src="http://www.j9p.com/images/6.gif" alt="好" width="24" height="24" data-face-id="6"/>
<img src="http://www.j9p.com/images/7.gif" alt="下下下" width="24" height="24" data-face-id="7"/>
<img src="http://www.j9p.com/images/8.gif" alt="送花" width="24" height="24" data-face-id="8"/>
<img src="http://www.j9p.com/images/9.gif" alt="屎" width="24" height="24" data-face-id="9"/>
<img src="http://www.j9p.com/images/10.gif" alt="亲亲" width="24" height="24" data-face-id="10"/>
</div>
<textarea name="ly_content" id="ly_content"></textarea>
<div class="comment_btn">
<span class="word_count">字数: <b id="ly_num">0</b>/500</span>
<input id="comment_button" type="button" value=" 发表评论 " />(您的评论需要经过审核才能显示)
</div>
</form>
</div>
</div>
</div>
</dt>
<dd class="g-softcontent-right">
<div class="m-rmjx">
<p class="title"><strong>同类软件</strong></p>
<ul>
<li><a href="/down/524058.html" preview="http://pic.j9p.com/up/2020-4/202041111357764860.png" target="_blank"><img class="tu" src="http://pic.j9p.com/up/2020-4/2020411113512790.jpg" alt="小数据之美pdf"><strong class="name">小数据之美pdf</strong><em class="info">18.5M/免费下载</em></a></li><li><a href="/down/525187.html" preview="http://pic.j9p.com/up/2020-5/202052114129320420.png" target="_blank"><img class="tu" src="http://pic.j9p.com/up/2020-5/2020521140453938.jpg" alt="干掉失眠：让你睡个好觉的心理疗法PDF"><strong class="name">干掉失眠：让你睡个好觉的心理疗法PDF</strong><em class="info">18.5M/电子书</em></a></li><li><a href="/down/525039.html" preview="http://pic.j9p.com/up/2020-4/2020427173523653750.png" target="_blank"><img class="tu" src="http://pic.j9p.com/up/2020-4/20204271735143561.png" alt="成为数据分析师pdf"><strong class="name">成为数据分析师pdf</strong><em class="info">18.5M/</em></a></li><li><a href="/down/525037.html" preview="http://pic.j9p.com/up/2020-4/2020427171543552640.png" target="_blank"><img class="tu" src="http://pic.j9p.com/up/2020-4/20204271715332672.png" alt="我们老了怎么办:让你晚年富足的理财计划pdf"><strong class="name">我们老了怎么办:让你晚年富足的理财计划pdf</strong><em class="info">18.5M/</em></a></li><li><a href="/down/525021.html" preview="http://pic.j9p.com/up/2020-4/202042714587764860.png" target="_blank"><img class="tu" src="http://pic.j9p.com/up/2020-4/2020427152262171.png" alt="首席增长官：如何用数据驱动增长PDF下载"><strong class="name">首席增长官：如何用数据驱动增长PDF下载</strong><em class="info">18.5M/</em></a></li>
</ul>
</div>
<div class="m-rmtj">
<p class="title"><strong>相关软件</strong> <span class="change">换一批</span></p>
<ul>
<li><a href="/down/525501.html"><img src="http://pic.j9p.com/up/2020-5/20205111337155799.jpg" alt="淘宝天猫SEO从入门到精通pdf下载"><p>淘宝天猫SEO从入门到精通pdf下载</p></a></li><li><a href="/down/525409.html"><img src="http://pic.j9p.com/up/2020-5/202059101153539.png" alt="燃点：正在发生的创业史pdf下载"><p>燃点：正在发生的创业史pdf下载</p></a></li><li><a href="/down/525405.html"><img src="http://pic.j9p.com/up/2020-5/2020599353836.png" alt="智能与智慧PDF"><p>智能与智慧PDF</p></a></li><li><a href="/down/525354.html"><img src="http://pic.j9p.com/up/2020-5/2020581358354797.png" alt="大型网站服务器容量规划pdf下载"><p>大型网站服务器容量规划pdf下载</p></a></li><li><a href="/down/525346.html"><img src="http://pic.j9p.com/up/2020-5/202058113487926.png" alt="大教堂与集市pdf"><p>大教堂与集市pdf</p></a></li><li><a href="/down/525332.html"><img src="http://pic.j9p.com/up/2020-5/202058943544707.png" alt="人人都该懂的互联网思维PDF"><p>人人都该懂的互联网思维PDF</p></a></li><li><a href="/down/525299.html"><img src="http://pic.j9p.com/up/2020-5/202057162293750.jpg" alt="工具，还是武器？PDF"><p>工具，还是武器？PDF</p></a></li><li><a href="/down/525266.html"><img src="http://pic.j9p.com/up/2020-5/2020571012488733.jpg" alt="孙正义传：打造300年企业帝国的野心"><p>孙正义传：打造300年企业帝国的野心</p></a></li><li><a href="/down/525139.html"><img src="http://pic.j9p.com/up/2020-4/20204291124278332.png" alt="轻营销：小预算玩转大市场(第3版)"><p>轻营销：小预算玩转大市场(第3版)</p></a></li>
</ul>
<ul style="display:none;">
<li><a href="/down/525039.html"><img src="http://pic.j9p.com/up/2020-4/20204271735143561.png" alt="成为数据分析师pdf"><p>成为数据分析师pdf</p></a></li><li><a href="/down/525020.html"><img src="http://pic.j9p.com/up/2020-4/2020427156315908.png" alt="18个未来进行时pdf"><p>18个未来进行时pdf</p></a></li><li><a href="/down/524984.html"><img src="http://pic.j9p.com/up/2020-4/20204261956181649.jpg" alt="大数据营销：定位客户PDF"><p>大数据营销：定位客户PDF</p></a></li><li><a href="/down/524976.html"><img src="http://pic.j9p.com/up/2020-4/20204261749501373.png" alt="崛起的超级智能pdf"><p>崛起的超级智能pdf</p></a></li><li><a href="/down/524954.html"><img src="http://pic.j9p.com/up/2020-4/20204261429567465.png" alt="区块链金融应用发展白皮书PDF电子书"><p>区块链金融应用发展白皮书PDF电子书</p></a></li><li><a href="/down/524951.html"><img src="http://pic.j9p.com/up/2020-4/2020426146491360.png" alt="社群营销与运营pdf"><p>社群营销与运营pdf</p></a></li><li><a href="/down/524949.html"><img src="http://pic.j9p.com/up/2020-4/2020426135037067.png" alt="人人时代：无组织的组织力量pdf下载"><p>人人时代：无组织的组织力量pdf下载</p></a></li><li><a href="/down/524943.html"><img src="http://pic.j9p.com/up/2020-4/2020426113733512.png" alt="穿越计算机的迷雾pdf"><p>穿越计算机的迷雾pdf</p></a></li><li><a href="/down/524939.html"><img src="http://pic.j9p.com/up/2020-4/2020426112172541.jpg" alt="明智转向：数字时代的转型思维和增长模式"><p>明智转向：数字时代的转型思维和增长模式</p></a></li>
</ul>
</div>
<div class="m-top">
<p class="title"><strong>软件TOP榜</strong></p>
<ul>
<li>
<em>1</em>
<div>
<a href="/down/525516.html">
<img src="http://pic.j9p.com/up/2020-5/2020513834416303.png" alt="数据中台：让数据用起来pdf下载">
<strong>数据中台：让数据用起来pdf下载</strong>
<span>立即下载</span>
</a>
</div>
<p>数据中台：让数据用起来pdf下载</p>
</li><li>
<em>2</em>
<div>
<a href="/down/525501.html">
<img src="http://pic.j9p.com/up/2020-5/20205111337155799.jpg" alt="淘宝天猫SEO从入门到精通pdf下载">
<strong>淘宝天猫SEO从入门到精通pdf下载</strong>
<span>立即下载</span>
</a>
</div>
<p>淘宝天猫SEO从入门到精通pdf下载</p>
</li><li>
<em>3</em>
<div>
<a href="/down/525409.html">
<img src="http://pic.j9p.com/up/2020-5/202059101153539.png" alt="燃点：正在发生的创业史pdf下载">
<strong>燃点：正在发生的创业史pdf下载</strong>
<span>立即下载</span>
</a>
</div>
<p>燃点：正在发生的创业史pdf下载</p>
</li><li>
<em>4</em>
<div>
<a href="/down/525405.html">
<img src="http://pic.j9p.com/up/2020-5/2020599353836.png" alt="智能与智慧PDF电子书">
<strong>智能与智慧PDF</strong>
<span>立即下载</span>
</a>
</div>
<p>智能与智慧PDF电子书</p>
</li><li>
<em>5</em>
<div>
<a href="/down/525354.html">
<img src="http://pic.j9p.com/up/2020-5/2020581358354797.png" alt="大型网站服务器容量规划pdf下载">
<strong>大型网站服务器容量规划pdf下载</strong>
<span>立即下载</span>
</a>
</div>
<p>大型网站服务器容量规划pdf下载</p>
</li><li>
<em>6</em>
<div>
<a href="/down/525346.html">
<img src="http://pic.j9p.com/up/2020-5/202058113487926.png" alt="大教堂与集市pdf最新版">
<strong>大教堂与集市pdf</strong>
<span>立即下载</span>
</a>
</div>
<p>大教堂与集市pdf最新版</p>
</li><li>
<em>7</em>
<div>
<a href="/down/525332.html">
<img src="http://pic.j9p.com/up/2020-5/202058943544707.png" alt="人人都该懂的互联网思维PDF电子书">
<strong>人人都该懂的互联网思维PDF</strong>
<span>立即下载</span>
</a>
</div>
<p>人人都该懂的互联网思维PDF电子书</p>
</li><li>
<em>8</em>
<div>
<a href="/down/525299.html">
<img src="http://pic.j9p.com/up/2020-5/202057162293750.jpg" alt="工具，还是武器？PDF电子书下载">
<strong>工具，还是武器？PDF</strong>
<span>立即下载</span>
</a>
</div>
<p>工具，还是武器？PDF电子书下载</p>
</li><li>
<em>9</em>
<div>
<a href="/down/525266.html">
<img src="http://pic.j9p.com/up/2020-5/2020571012488733.jpg" alt="孙正义传：打造300年企业帝国的野心电子书">
<strong>孙正义传：打造300年企业帝国的野心</strong>
<span>立即下载</span>
</a>
</div>
<p>孙正义传：打造300年企业帝国的野心电子书</p>
</li><li>
<em>10</em>
<div>
<a href="/down/525139.html">
<img src="http://pic.j9p.com/up/2020-4/20204291124278332.png" alt="轻营销：小预算玩转大市场(第3版)电子书">
<strong>轻营销：小预算玩转大市场(第3版)</strong>
<span>立即下载</span>
</a>
</div>
<p>轻营销：小预算玩转大市场(第3版)电子书</p>
</li>
</ul>
</div>
</dd>
</dl>
<div id="footer" class="g-footer">
<p><a href="http://www.j9p.com/about.html">关于我们</a>|<a href="http://www.j9p.com/content.html">联系方式</a> | <a href="http://www.j9p.com/help.html">下载帮助</a> | <a href="http://www.j9p.com/class/">网站地图</a></p>
<p><span>精品下载</span> <span>Copyright(C) 2018-2020 www.j9p.com All Rights Reserved!</span></p> <p><span>网站备案/许可证号: 鄂ICP备17009381号-1</span></p>
</div>
<div style="display:none"><script language="javascript" src="/js/count.js"></script></div>
<script src="/js/comment.js"></script>
<script type="text/javascript">voteuzzf("525516"); </script>
<script src="/js/base.js"></script>
</body>
</html>

"""
parse_html = etree.parse(html, etree.HTMLParser())
# TODO 链接 <ul class="ul_Address"><script type="text/javascript" src="/inc/downLoad.asp?Address=tetjsxnx%2Ezip&TypeID=1&SoftLinkID=15732&SoftID=524538"></script></ul>
# ul_Address = parse_html.xpath("//ul[@class='ul_Address']/script/@src")
ul_Address = parse_html.xpath("//ul[@class='ul_Address']")
print(ul_Address[0])
query_result = urlparse(ul_Address[0]).query
query_address = parse_qs(query_result).get("Address")
pdf_Address = "http://jxz1.j9p.com/pc/" + query_address[0]
print(pdf_Address)
