import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from mpl_toolkits.mplot3d import Axes3D
# TODO 一个窗口多个图
# 一个窗口，多个图，多条数据
sub1 = plt.subplot(211, facecolor=(0.1843, 0.3098, 0.3098))  # 将窗口分成2行1列，在第1个作图，并设置背景色
sub2 = plt.subplot(212)  # 将窗口分成2行1列，在第2个作图
sub1.plot(x, y)  # 绘制子图
sub2.plot(x, y)  # 绘制子图

axes1 = plt.axes([.2, .3, .1, .1], facecolor='y')  # 添加一个子坐标系，rect=[左, 下, 宽, 高]
plt.plot(x, y)  # 绘制子坐标系，
axes2 = plt.axes([0.7, .2, .1, .1], facecolor='y')  # 添加一个子坐标系，rect=[左, 下, 宽, 高]
plt.plot(x, y)
plt.show()