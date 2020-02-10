# TODO https://www.jianshu.com/p/da385a35f68d
#  https://blog.csdn.net/luanpeng825485697/article/details/78508819
#  https://www.runoob.com/w3cnote/matplotlib-tutorial.html
# TODO 配置参数：
# axex: 设置坐标轴边界和表面的颜色、坐标刻度值大小和网格的显示
# figure: 控制dpi、边界颜色、图形大小、和子区( subplot)设置
# font: 字体集（font family）、字体大小和样式设置
# grid: 设置网格颜色和线性
# legend: 设置图例和其中的文本的显示
# line: 设置线条（颜色、线型、宽度等）和标记
# patch: 是填充2D空间的图形对象，如多边形和圆。控制线宽、颜色和抗锯齿设置等。
# savefig: 可以对保存的图形进行单独设置。例如，设置渲染的文件的背景为白色。
# verbose: 设置matplotlib在执行期间信息输出，如silent、helpful、debug和debug-annoying。
# xticks和yticks: 为x,y轴的主刻度和次刻度设置颜色、大小、方向，以及标签大小。

# TODO 线条标记标记maker            描述
#
# ‘o’                 圆圈
# ‘.’                 点
# ‘D’                 菱形
# ‘s’                 正方形
# ‘h’                 六边形1
# ‘*’                 星号
# ‘H’                 六边形2
# ‘d’                 小菱形
# ‘_’                 水平线
# ‘v’                 一角朝下的三角形
# ‘8’                 八边形
# ‘<’                 一角朝左的三角形
# ‘p’                 五边形
# ‘>’                 一角朝右的三角形
# ‘,’                 像素
# ‘^’                 一角朝上的三角形
# ‘+’                 加号
# ‘\  ‘               竖线
# ‘None’,’’,’ ‘       无
# ‘x’                 X

# TODO 颜色
# 别名             颜色
#
# b               蓝色
# g               绿色
# r               红色
# y               黄色
# c               青色
# k               黑色
# m               洋红色
# w               白色

# 如果这两种颜色不够用，还可以通过两种其他方式来定义颜色值：
#
# 1、使用HTML十六进制字符串 color=’#123456’ 使用合法的HTML颜色名字（’red’,’chartreuse’等）。
# 2、也可以传入一个归一化到[0,1]的RGB元祖。 color=(0.3,0.3,0.4)


# TODO 背景色
# 通过向如matplotlib.pyplot.axes()或者matplotlib.pyplot.subplot()这样的方法提供一个axisbg参数，可以指定坐标这的背景色。
#
# subplot(111,axisbg=(0.1843,0.3098,0.3098)）
#
# 以下示例需要引入的库包括
#
#
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from mpl_toolkits.mplot3d import Axes3D

# TODO 绘图操作步骤（以点图、线图为例）
# 使用numpy产生数据
x = np.arange(-5, 5, 0.1)
y = x * 3

# 创建窗口、子图
# 方法1：先创建窗口，再创建子图。（一定绘制）
fig = plt.figure(num=1, figsize=(15, 8), dpi=80)  # 开启一个窗口，同时设置大小，分辨率
ax1 = fig.add_subplot(2, 1, 1)  # 通过fig添加子图，参数：行数，列数，第几个。
ax2 = fig.add_subplot(2, 1, 2)  # 通过fig添加子图，参数：行数，列数，第几个。
print(fig, ax1, ax2)
# 方法2：一次性创建窗口和多个子图。（空白不绘制）
fig, axarr = plt.subplots(4, 1)  # 开一个新窗口，并添加4个子图，返回子图数组
ax1 = axarr[0]  # 通过子图数组获取一个子图
print(fig, ax1)
# 方法3：一次性创建窗口和一个子图。（空白不绘制）
ax1 = plt.subplot(1, 1, 1, facecolor='white')  # 开一个新窗口，创建1个子图。facecolor设置背景颜色
print(ax1)
# 获取对窗口的引用，适用于上面三种方法
# fig = plt.gcf()   #获得当前figure
# fig=ax1.figure   #获得指定子图所属窗口

# fig.subplots_adjust(left=0)                         #设置窗口左内边距为0，即左边留白为0。

# 设置子图的基本元素
ax1.set_title('python-drawing')  # 设置图体，plt.title
ax1.set_xlabel('x-name')  # 设置x轴名称,plt.xlabel
ax1.set_ylabel('y-name')  # 设置y轴名称,plt.ylabel
plt.axis([-6, 6, -10, 10])  # 设置横纵坐标轴范围，这个在子图中被分解为下面两个函数
ax1.set_xlim(-5, 5)  # 设置横轴范围，会覆盖上面的横坐标,plt.xlim
ax1.set_ylim(-10, 10)  # 设置纵轴范围，会覆盖上面的纵坐标,plt.ylim

xmajorLocator = MultipleLocator(2)  # 定义横向主刻度标签的刻度差为2的倍数。就是隔几个刻度才显示一个标签文本
ymajorLocator = MultipleLocator(3)  # 定义纵向主刻度标签的刻度差为3的倍数。就是隔几个刻度才显示一个标签文本

ax1.xaxis.set_major_locator(xmajorLocator)  # x轴 应用定义的横向主刻度格式。如果不应用将采用默认刻度格式
ax1.yaxis.set_major_locator(ymajorLocator)  # y轴 应用定义的纵向主刻度格式。如果不应用将采用默认刻度格式

ax1.xaxis.grid(True, which='major')  # x坐标轴的网格使用定义的主刻度格式
ax1.yaxis.grid(True, which='major')  # x坐标轴的网格使用定义的主刻度格式

ax1.set_xticks([])  # 去除坐标轴刻度
ax1.set_xticks((-5, -3, -1, 1, 3, 5))  # 设置坐标轴刻度
ax1.set_xticklabels(labels=['x1', 'x2', 'x3', 'x4', 'x5'], rotation=-30,
                    fontsize='small')  # 设置刻度的显示文本，rotation旋转角度，fontsize字体大小

plot1 = ax1.plot(x, y, marker='o', color='g', label='legend1')  # 点图：marker图标
plot2 = ax1.plot(x, y, linestyle='--', alpha=0.5, color='r',
                 label='legend2')  # 线图：linestyle线性，alpha透明度，color颜色，label图例文本

ax1.legend(loc='upper left')  # 显示图例,plt.legend()
ax1.text(2.8, 7, r'y=3*x')  # 指定位置显示文字,plt.text()
ax1.annotate('important point', xy=(2, 6), xytext=(3, 1.5),  # 添加标注，参数：注释文本、指向点、文字位置、箭头属性
             arrowprops=dict(facecolor='black', shrink=0.05),
             )
# 显示网格。which参数的值为major(只绘制大刻度)、minor(只绘制小刻度)、both，默认值为major。axis为'x','y','both'
ax1.grid(b=True, which='major', axis='both', alpha=0.5, color='skyblue', linestyle='--', linewidth=2)

axes1 = plt.axes([.2, .3, .1, .1], facecolor='y')  # 在当前窗口添加一个子图，rect=[左, 下, 宽, 高]，是使用的绝对布局，不和以存在窗口挤占空间
axes1.plot(x, y)  # 在子图上画图
# plt.savefig('aa.jpg', dpi=400, bbox_inches='tight')  # savefig保存图片，dpi分辨率，bbox_inches子图周边白色空间的大小
# plt.show()  # 打开窗口，对于方法1创建在窗口一定绘制，对于方法2方法3创建的窗口，若坐标系全部空白，则不绘制

# TODO plot时可以设置的属性包括如下：
# 属性                      值类型
# alpha                   浮点值
# animated                [True / False]
# antialiased or aa       [True / False]
# clip_box                matplotlib.transform.Bbox 实例
# clip_on                 [True / False]
# clip_path               Path 实例， Transform，以及Patch实例
# color or c              任何 matplotlib 颜色
# contains                命中测试函数
# dash_capstyle           ['butt' / 'round' / 'projecting']
# dash_joinstyle          ['miter' / 'round' / 'bevel']
# dashes                  以点为单位的连接/断开墨水序列
# data                    (np.array xdata, np.array ydata)
# figure                  matplotlib.figure.Figure 实例
# label                   任何字符串
# linestyle or ls         [ '-' / '--' / '-.' / ':' / 'steps' / ...]
# linewidth or lw         以点为单位的浮点值
# lod                     [True / False]
# marker                  [ '+' / ',' / '.' / '1' / '2' / '3' / '4' ]
# markeredgecolor or mec  任何 matplotlib 颜色
# markeredgewidth or mew  以点为单位的浮点值
# markerfacecolor or mfc  任何 matplotlib 颜色
# markersize or ms        浮点值
# markevery               [ None / 整数值 / (startind, stride) ]
# picker                  用于交互式线条选择
# pickradius              线条的拾取选择半径
# solid_capstyle          ['butt' / 'round' / 'projecting']
# solid_joinstyle         ['miter' / 'round' / 'bevel']
# transform               matplotlib.transforms.Transform 实例
# visible                 [True / False]
# xdata                   np.array
# ydata                   np.array
# zorder                  任何数值


from pylab import *

subplot(2,2,1)
xticks([]), yticks([])
text(0.5,0.5, 'subplot(2,2,1)',ha='center',va='center',size=20,alpha=.5)

subplot(2,2,2)
xticks([]), yticks([])
text(0.5,0.5, 'subplot(2,2,2)',ha='center',va='center',size=20,alpha=.5)

subplot(2,2,3)
xticks([]), yticks([])
text(0.5,0.5, 'subplot(2,2,3)',ha='center',va='center',size=20,alpha=.5)

subplot(2,2,4)
xticks([]), yticks([])
text(0.5,0.5, 'subplot(2,2,4)',ha='center',va='center',size=20,alpha=.5)

# savefig('../figures/subplot-grid.png', dpi=64)
show()


