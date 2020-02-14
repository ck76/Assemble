from __future__ import print_function   # 从future版本导入print函数功能
import argparse                         # 加载处理命令行参数的库
import torch                            # 引入相关的包
import torch.nn as nn                   # 指定torch.nn别名nn
import torch.nn.functional as F         # 引用神经网络常用函数包，不具有可学习的参数
import torch.optim as optim
from torch.autograd import Variable
from torchvision import datasets, transforms  # 加载pytorch官方提供的dataset

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from mpl_toolkits.mplot3d import Axes3D

x = torch.linspace(-5, 5, 200) # x data(tensor), shape(100,1)
print(x)
# x = Variable(x)
x_np = x.data.numpy()    # 转成 numpy array，出图时用

# 几种常用的激励函数
y_relu = F.relu(x).data.numpy()
# y_sigmoid = F.sigmoid(x).data.numpy()
y_sigmoid=torch.sigmoid(x).data.numpy()
y_tanh = F.tanh(x).data.numpy()
y_softplus = F.softplus(x).data.numpy()
# y_softmax = F.softmax(x).data.numpy  softmax 比较特殊，不能直接显示，用于多分类

# 画图
plt.figure(1, figsize=(8, 6))  # 作用新建绘画窗口,独立显示绘画的图片
plt.subplot(2,3,1)
plt.plot(x_np, y_relu, c='red', label='relu')
plt.ylim(-1, 5)    # 设置 y 轴范围
plt.legend(loc="best")  # 显示图例，best 为自适应

plt.subplot(232)
plt.plot(x_np, y_sigmoid, c='red', label='sigmoid')
plt.ylim(-0.2, 1.2)
plt.legend(loc="best")

plt.subplot(233)
plt.plot(x_np, y_tanh, c='red', label='tanh')
plt.ylim(-1.2, 1.2)
plt.legend(loc="best")

plt.subplot(224)
plt.plot(x_np, y_softplus, c='red', label='softplus')
plt.ylim(-0.2, 6)
plt.legend(loc="best")

plt.show()