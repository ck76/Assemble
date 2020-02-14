# TODO https://www.cnblogs.com/wj-1314/p/9842719.html

import argparse                         # 加载处理命令行参数的库
import torch                            # 引入相关的包
import torch.nn as nn                   # 指定torch.nn别名nn
import torch.nn.functional as F         # 引用神经网络常用函数包，不具有可学习的参数
import torch.optim as optim
import torchvision
import matplotlib as plt
import numpy as np
from torch.autograd import Variable
from torchvision import datasets, transforms  # 加载pytorch官方提供的dataset

#transform = transforms.Compose(
#     [transforms.ToTensor(),
#      transforms.Lambda(lambda x: x.repeat(3, 1, 1)),
#      transforms.Normalize(mean=(0.5, 0.5, 0.5), std=(0.5, 0.5, 0.5))])
transform = transforms.Compose([
     transforms.ToTensor(),
     transforms.Lambda(lambda x: x.repeat(3,1,1)),
     transforms.Normalize(mean=(0.5, 0.5, 0.5), std=(0.5, 0.5, 0.5))
 ])   # 修改的位置

trainset = torchvision.datasets.MNIST(root='~/Datasets', train=True,
                                        download=True, transform=transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=4,
                                          shuffle=True, num_workers=2)

testset = torchvision.datasets.MNIST(root='~/Datasets', train=False,
                                       download=True, transform=transform)
testloader = torch.utils.data.DataLoader(testset, batch_size=4,
                                         shuffle=False, num_workers=2)

# 在装载完成后，我们可以选取其中一个批次的数据进行预览
# images, labels = next(iter(trainloader))
# img = torchvision.utils.make_grid(images)
#
# img = img.numpy().transpose(1, 2, 0)
# std = [0.5, 0.5, 0.5]
# mean = [0.5, 0.5, 0.5]
# img = img * std + mean
# print(labels)
# # print([labels[i] for i in range(64)])
# # 由于matplotlab中的展示图片无法显示，所以现在使用OpenCV中显示图片
# plt.imshow(img)
#
# images, labels = next(iter(trainloader))
# img = torchvision.utils.make_grid(images)
#
# img = img.numpy().transpose(1, 2, 0)
# std = [0.5, 0.5, 0.5]
# mean = [0.5, 0.5, 0.5]
# img = img * std + mean
# print([labels[i] for i in range(64)])
# plt.imshow(img)

print(type(trainset))
print(len(trainset), len(testset))

# print(type((trainset[0])))
# print(trainset[0])
# print('---',torch.from_numpy(np.array(trainset)).shape)
# feature, label = trainset[0]
# print(feature.shape, feature.dtype)  # Channel x Height X Width
# print(label)
