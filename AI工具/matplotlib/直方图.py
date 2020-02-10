import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from mpl_toolkits.mplot3d import Axes3D

# TODO 直方图
fig, (ax0, ax1) = plt.subplots(nrows=2, figsize=(9, 6))  # 在窗口上添加2个子图
sigma = 1  # 标准差
mean = 0  # 均值
x = mean + sigma * np.random.randn(10000)  # 正态分布随机数
ax0.hist(x, bins=40, normed=False, histtype='bar', facecolor='yellowgreen',
         alpha=0.75)  # normed是否归一化，histtype直方图类型，facecolor颜色，alpha透明度
ax1.hist(x, bins=20, normed=1, histtype='bar', facecolor='pink', alpha=0.75, cumulative=True,
         rwidth=0.8)  # bins柱子的个数,cumulative是否计算累加分布，rwidth柱子宽度
plt.show()  # 所有窗口运行