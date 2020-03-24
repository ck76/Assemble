# https://blog.csdn.net/dss_dssssd/article/details/82980222
# https://blog.csdn.net/qq_27825451/article/details/90551513
"""
一个有序的容器，神经网络模块将按照在传入构造器的顺序依次被添加到计算图中执行，同时以神经网络模块为元素的有序字典也可以作为传入参数。
"""
# Example of using Sequential
from collections import OrderedDict

from torch import nn

model = nn.Sequential(
    nn.Conv2d(1, 20, 5),
    nn.ReLU(),
    nn.Conv2d(20, 64, 5),
    nn.ReLU()
)

# Example of using Sequential with OrderedDict
model = nn.Sequential(OrderedDict([
    ('conv1', nn.Conv2d(1, 20, 5)),
    ('relu1', nn.ReLU()),
    ('conv2', nn.Conv2d(20, 64, 5)),
    ('relu2', nn.ReLU())
]))

"""下面是简单的三层网络结构的例子："""
# hyper parameters
in_dim = 1
n_hidden_1 = 1
n_hidden_2 = 1
out_dim = 1

class Net(nn.Module):
    def __init__(self, in_dim, n_hidden_1, n_hidden_2, out_dim):
        super().__init__()

        self.layer = nn.Sequential(
            nn.Linear(in_dim, n_hidden_1),
            nn.ReLU(True),
            nn.Linear(n_hidden_1, n_hidden_2),
            nn.ReLU(True),
            # 最后一层不需要添加激活函数
            nn.Linear(n_hidden_2, out_dim)
        )

    def forward(self, x):
        """上面的代码就是通过Squential将网络层和激活函数结合起来，输出激活后的网络节点。"""
        x = self.layer(x)
        return x
"""
class Sequential(Module): # 继承Module
    def __init__(self, *args):  # 重写了构造函数
    def _get_item_by_idx(self, iterator, idx):
    def __getitem__(self, idx):
    def __setitem__(self, idx, module):
    def __delitem__(self, idx):
    def __len__(self):
    def __dir__(self):
    def forward(self, input):  # 重写关键方法forward
    """

"""
除此之外
class Container(Module):
class Sequential(Module)：
class ModuleList(Module)：
class ModuleDict(Module):
class ParameterList(Module):
class ParameterDict(Module):
"""

"""
最简单的序贯模型"""
import torch.nn as nn

model = nn.Sequential(
    nn.Conv2d(1, 20, 5),
    nn.ReLU(),
    nn.Conv2d(20, 64, 5),
    nn.ReLU()
)

print(model)
print(model[2])  # 通过索引获取第几个层
'''运行结果为：
Sequential(
  (0): Conv2d(1, 20, kernel_size=(5, 5), stride=(1, 1))
  (1): ReLU()
  (2): Conv2d(20, 64, kernel_size=(5, 5), stride=(1, 1))
  (3): ReLU()
)
Conv2d(20, 64, kernel_size=(5, 5), stride=(1, 1))
'''

"""
给每一个层添加名称"""
import torch.nn as nn
from collections import OrderedDict

model = nn.Sequential(OrderedDict([
    ('conv1', nn.Conv2d(1, 20, 5)),
    ('relu1', nn.ReLU()),
    ('conv2', nn.Conv2d(20, 64, 5)),
    ('relu2', nn.ReLU())
]))

print(model)
print(model[2])  # 通过索引获取第几个层
'''运行结果为：
Sequential(
  (conv1): Conv2d(1, 20, kernel_size=(5, 5), stride=(1, 1))
  (relu1): ReLU()
  (conv2): Conv2d(20, 64, kernel_size=(5, 5), stride=(1, 1))
  (relu2): ReLU()
)
Conv2d(20, 64, kernel_size=(5, 5), stride=(1, 1))
'''


model = nn.Sequential()
model.add_module("conv1", nn.Conv2d(1, 20, 5))
model.add_module('relu1', nn.ReLU())
model.add_module('conv2', nn.Conv2d(20, 64, 5))
model.add_module('relu2', nn.ReLU())

print(model)
print(model[2])  # 通过索引获取第几个层




net = MySequential(
        nn.Linear(784, 256),
        nn.ReLU(),
        nn.Linear(256, 10),
        )
print(net)
net(X)
# MySequential(
#   (0): Linear(in_features=784, out_features=256, bias=True)
#   (1): ReLU()
#   (2): Linear(in_features=256, out_features=10, bias=True)
# )
# tensor([[ 0.1883, -0.1269, -0.1886,  0.0638, -0.1004, -0.0600,  0.0760, -0.1788,
#          -0.1844, -0.2131],
#         [ 0.1319, -0.0490, -0.1365,  0.0133, -0.0483, -0.0861,  0.0369, -0.0830,
#          -0.0462, -0.2066]], grad_fn=<ThAddmmBackward>)

# TODO ModuleList类
net = nn.ModuleList([nn.Linear(784, 256), nn.ReLU()])
net.append(nn.Linear(256, 10)) # # 类似List的append操作
print(net[-1])  # 类似List的索引访问
print(net)
# Linear(in_features=256, out_features=10, bias=True)
# ModuleList(
#   (0): Linear(in_features=784, out_features=256, bias=True)
#   (1): ReLU()
#   (2): Linear(in_features=256, out_features=10, bias=True)
# )

# TODO ModuleDict
net = nn.ModuleDict({
    'linear': nn.Linear(784, 256),
    'act': nn.ReLU(),
})
net['output'] = nn.Linear(256, 10) # 添加
print(net['linear']) # 访问
print(net.output)
print(net)

# Linear(in_features=784, out_features=256, bias=True)
# Linear(in_features=256, out_features=10, bias=True)
# ModuleDict(
#   (act): ReLU()
#   (linear): Linear(in_features=784, out_features=256, bias=True)
#   (output): Linear(in_features=256, out_features=10, bias=True)
# )