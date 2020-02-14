# TODO https://pytorch.apachecn.org/docs/1.2/beginner/saving_loading_models.html
"""
关于保存和加载模型，有三个核心功能需要熟悉：

torch.save：将序列化的对象保存到磁盘。此函数使用Python的 pickle实用程序进行序列化。使用此功能可以保存各种对象的模型，张量和字典。
torch.load：使用pickle的解腌功能将腌制的目标文件反序列化到内存中。此功能还有助于设备将数据加载到其中（请参阅 跨设备保存和加载模型）。
torch.nn.load_state_dict：使用反序列化的state_dict加载模型的参数字典 。有关state_dict的更多信息，请参阅什么是state_dict？。
"""
from __future__ import print_function, division
import os
import torch
import pandas as pd
from skimage import io, transform
import numpy as np
import matplotlib.pyplot as plt
from torch import nn
from torch import functional as F
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms, utils
import matplotlib.pyplot as plt
import numpy as np

import torch
import torchvision
import torchvision.transforms as transforms

import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim


# Define model
class TheModelClass(nn.Module):
    def __init__(self):
        super(TheModelClass, self).__init__()
        self.conv1 = nn.Conv2d(3, 6, 5)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, 16 * 5 * 5)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x


# Initialize model
model = TheModelClass()

# Initialize optimizer
optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)

# Print model's state_dict
print("Model's state_dict:")
for param_tensor in model.state_dict():
    print(param_tensor, "\t", model.state_dict()[param_tensor].size())

# Print optimizer's state_dict
print("Optimizer's state_dict:")
for var_name in optimizer.state_dict():
    print(var_name, "\t", optimizer.state_dict()[var_name])
"""
Model's state_dict:
conv1.weight 	 torch.Size([6, 3, 5, 5])
conv1.bias 	 torch.Size([6])
conv2.weight 	 torch.Size([16, 6, 5, 5])
conv2.bias 	 torch.Size([16])
fc1.weight 	 torch.Size([120, 400])
fc1.bias 	 torch.Size([120])
fc2.weight 	 torch.Size([84, 120])
fc2.bias 	 torch.Size([84])
fc3.weight 	 torch.Size([10, 84])
fc3.bias 	 torch.Size([10])

Optimizer's state_dict:
state 	 {}
param_groups 	 [{'lr': 0.001, 
                    'momentum': 0.9, 
                    'dampening': 0, 
                    'weight_decay': 0, 
                    'nesterov': False, 
                    'params': [5247640704, 5247640776, 5247640848, 5247640920, 5247640992, 5247641064, 5247641136, 5247641208, 5247641280, 5247641352]}]
"""

torch.save(model.state_dict(), '~/Datasets/save_model.pt')
model = TheModelClass()
model.load_state_dict(torch.load('~/Datasets/save_model.pt'))
model.eval()
"""
常见的PyTorch约定是使用.pt或 .pth文件扩展名保存模型。
请记住，model.eval()在运行推理之前，必须先调用以将退出和批处理规范化层设置为评估模式。不这样做将产生不一致的推断结果。"""


# TODO v保存和加载用于推理和/或继续训练的常规检查点
torch.save({
    # 'epoch': epoch,
    'model_state_dict': model.state_dict(),
    'optimizer_state_dict': optimizer.state_dict(),
    # 'loss': loss,
    }, '~/Datasets/save_model.pt')

checkpoint = torch.load('~/Datasets/save_model.pt')
model.load_state_dict(checkpoint['model_state_dict'])
optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
epoch = checkpoint['epoch']
loss = checkpoint['loss']

model.eval()
# - or -
model.train()

# TODO 将多个模型保存在一个文件中
"""
torch.save({
    'modelA_state_dict': modelA.state_dict(),
    'modelB_state_dict': modelB.state_dict(),
    'optimizerA_state_dict': optimizerA.state_dict(),
    'optimizerB_state_dict': optimizerB.state_dict(),
    ...
    }, PATH)
    
modelA = TheModelAClass(*args, **kwargs)
modelB = TheModelBClass(*args, **kwargs)
optimizerA = TheOptimizerAClass(*args, **kwargs)
optimizerB = TheOptimizerBClass(*args, **kwargs)

checkpoint = torch.load(PATH)
modelA.load_state_dict(checkpoint['modelA_state_dict'])
modelB.load_state_dict(checkpoint['modelB_state_dict'])
optimizerA.load_state_dict(checkpoint['optimizerA_state_dict'])
optimizerB.load_state_dict(checkpoint['optimizerB_state_dict'])

modelA.eval()
modelB.eval()
# - or -
modelA.train()
modelB.train()
    
"""

# TODO 保存CPU，加载在GPU
"""
device = torch.device("cuda")
model = TheModelClass()
model.load_state_dict(torch.load("'~/Datasets/save_model.pt'", map_location="cuda:0"))  # Choose whatever GPU device number you want
model.to(device)
# Make sure to call input = input.to(device) on any input tensors that you feed to the model
"""