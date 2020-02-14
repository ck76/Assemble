
# https://blog.csdn.net/qq_27825451/article/details/90550890
# 不管是自定义层、自定义块、自定义模型，都是通过继承Module类完成的，这一点很重要。其实Sequential类也是继承自Module类的。
"""
class Module(object):
    def __init__(self):
    def forward(self, *input):

    def add_module(self, name, module):
    def cuda(self, device=None):
    def cpu(self):
    def __call__(self, *input, **kwargs):
    def parameters(self, recurse=True):
    def named_parameters(self, prefix='', recurse=True):
    def children(self):
    def named_children(self):
    def modules(self):
    def named_modules(self, memo=None, prefix=''):
    def train(self, mode=True):
    def eval(self):
    def zero_grad(self):
    def __repr__(self):
    def __dir__(self):
'''
有一部分没有完全列出来
'''
"""

"""
我们在定义自已的网络的时候，需要继承nn.Module类，并重新实现构造函数__init__构造函数和forward这两个方法。但有一些注意技巧：

（1）一般把网络中  具有  可学习参数的层（如全连接层、卷积层等）放在构造函数__init__()中，当然我也可以吧不具有参数的层也放在里面；

（2）一般把  不具有  可学习参数的层(如ReLU、dropout、BatchNormanation层)可放在构造函数中，也可不放在构造函数中，如果不放在构造函数__init__里面，则在forward方法里面可以使用nn.functional来代替
    
（3）forward方法是必须要重写的，它是实现模型的功能，实现各个层之间的连接关系的核心。
"""

import torch


class MyNet(torch.nn.Module):
    def __init__(self):
        super(MyNet, self).__init__()  # 第一句话，调用父类的构造函数
        self.conv1 = torch.nn.Conv2d(3, 32, 3, 1, 1)
        self.relu1 = torch.nn.ReLU()
        self.max_pooling1 = torch.nn.MaxPool2d(2, 1)

        self.conv2 = torch.nn.Conv2d(3, 32, 3, 1, 1)
        self.relu2 = torch.nn.ReLU()
        self.max_pooling2 = torch.nn.MaxPool2d(2, 1)

        self.dense1 = torch.nn.Linear(32 * 3 * 3, 128)
        self.dense2 = torch.nn.Linear(128, 10)

    def forward(self, x):
        x = self.conv1(x)
        x = self.relu1(x)
        x = self.max_pooling1(x)
        x = self.conv2(x)
        x = self.relu2(x)
        x = self.max_pooling2(x)
        x = self.dense1(x)
        x = self.dense2(x)
        return x


model = MyNet()
print(model)
'''运行结果为：
MyNet(
  (conv1): Conv2d(3, 32, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
  (relu1): ReLU()
  (max_pooling1): MaxPool2d(kernel_size=2, stride=1, padding=0, dilation=1, ceil_mode=False)
  (conv2): Conv2d(3, 32, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
  (relu2): ReLU()
  (max_pooling2): MaxPool2d(kernel_size=2, stride=1, padding=0, dilation=1, ceil_mode=False)
  (dense1): Linear(in_features=288, out_features=128, bias=True)
  (dense2): Linear(in_features=128, out_features=10, bias=True)
)
'''
# TODO 注意：上面的是将所有的层都放在了构造函数__init__里面，但是只是定义了一系列的层，
#  各个层之间到底是什么连接关系并没有，而是在forward里面实现所有层的连接关系，当然这里依然是顺序连接的。
#  下面再来看一下一个例子：
import torch
import torch.nn.functional as F

class MyNet(torch.nn.Module):
    def __init__(self):
        super(MyNet, self).__init__()  # 第一句话，调用父类的构造函数
        self.conv1 = torch.nn.Conv2d(3, 32, 3, 1, 1)
        self.conv2 = torch.nn.Conv2d(3, 32, 3, 1, 1)

        self.dense1 = torch.nn.Linear(32 * 3 * 3, 128)
        self.dense2 = torch.nn.Linear(128, 10)

    def forward(self, x):
        x = self.conv1(x)
        x = F.relu(x)
        x = F.max_pool2d(x)
        x = self.conv2(x)
        x = F.relu(x)
        x = F.max_pool2d(x)
        x = self.dense1(x)
        x = self.dense2(x)
        return x


model = MyNet()
print(model)
'''运行结果为：
MyNet(
  (conv1): Conv2d(3, 32, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
  (conv2): Conv2d(3, 32, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
  (dense1): Linear(in_features=288, out_features=128, bias=True)
  (dense2): Linear(in_features=128, out_features=10, bias=True)
)
'''

# TODO 注意：此时，将没有训练参数的层没有放在构造函数里面了，所以这些层就不会出现在model里面，但是运行关系是在forward里面通过functional的方法实现的。

# TODO 总结：所有放在构造函数__init__里面的层的都是这个模型的“固有属性”.


# TODO torch.nn.Module类的的多种实现
import torch.nn as nn
from collections import OrderedDict
class MyNet(nn.Module):
    def __init__(self):
        super(MyNet, self).__init__()
        self.conv_block = nn.Sequential(
            nn.Conv2d(3, 32, 3, 1, 1),
            nn.ReLU(),
            nn.MaxPool2d(2))
        self.dense_block = nn.Sequential(
            nn.Linear(32 * 3 * 3, 128),
            nn.ReLU(),
            nn.Linear(128, 10)
        )

    # 在这里实现层之间的连接关系，其实就是所谓的前向传播
    def forward(self, x):
        conv_out = self.conv_block(x)
        res = conv_out.view(conv_out.size(0), -1)
        out = self.dense_block(res)
        return out


model = MyNet()
print(model)
'''运行结果为：
MyNet(
  (conv_block): Sequential(
    (0): Conv2d(3, 32, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (1): ReLU()
    (2): MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
  )
  (dense_block): Sequential(
    (0): Linear(in_features=288, out_features=128, bias=True)
    (1): ReLU()
    (2): Linear(in_features=128, out_features=10, bias=True)
  )
)
'''

# TODO 2222
import torch.nn as nn
from collections import OrderedDict

class MyNet(nn.Module):
    def __init__(self):
        super(MyNet, self).__init__()
        self.conv_block = nn.Sequential(
            OrderedDict(
                [
                    ("conv1", nn.Conv2d(3, 32, 3, 1, 1)),
                    ("relu1", nn.ReLU()),
                    ("pool", nn.MaxPool2d(2))
                ]
            ))

        self.dense_block = nn.Sequential(
            OrderedDict([
                ("dense1", nn.Linear(32 * 3 * 3, 128)),
                ("relu2", nn.ReLU()),
                ("dense2", nn.Linear(128, 10))
            ])
        )

    def forward(self, x):
        conv_out = self.conv_block(x)
        res = conv_out.view(conv_out.size(0), -1)
        out = self.dense_block(res)
        return out


model = MyNet()
print(model)
'''运行结果为：
MyNet(
  (conv_block): Sequential(
    (conv1): Conv2d(3, 32, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (relu1): ReLU()
    (pool): MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
  )
  (dense_block): Sequential(
    (dense1): Linear(in_features=288, out_features=128, bias=True)
    (relu2): ReLU()
    (dense2): Linear(in_features=128, out_features=10, bias=True)
  )
)
'''

# TODO 333
import torch.nn as nn
from collections import OrderedDict


class MyNet(nn.Module):
    def __init__(self):
        super(MyNet, self).__init__()
        self.conv_block = torch.nn.Sequential()
        self.conv_block.add_module("conv1", torch.nn.Conv2d(3, 32, 3, 1, 1))
        self.conv_block.add_module("relu1", torch.nn.ReLU())
        self.conv_block.add_module("pool1", torch.nn.MaxPool2d(2))

        self.dense_block = torch.nn.Sequential()
        self.dense_block.add_module("dense1", torch.nn.Linear(32 * 3 * 3, 128))
        self.dense_block.add_module("relu2", torch.nn.ReLU())
        self.dense_block.add_module("dense2", torch.nn.Linear(128, 10))

    def forward(self, x):
        conv_out = self.conv_block(x)
        res = conv_out.view(conv_out.size(0), -1)
        out = self.dense_block(res)
        return out


model = MyNet()
print(model)
'''运行结果为：
MyNet(
  (conv_block): Sequential(
    (conv1): Conv2d(3, 32, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (relu1): ReLU()
    (pool1): MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
  )
  (dense_block): Sequential(
    (dense1): Linear(in_features=288, out_features=128, bias=True)
    (relu2): ReLU()
    (dense2): Linear(in_features=128, out_features=10, bias=True)
  )
)
'''

