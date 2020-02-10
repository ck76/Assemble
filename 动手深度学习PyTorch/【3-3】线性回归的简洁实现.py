import torch
from torch import nn
import numpy as np
import d2lzh_pytorch as d2l

d2l.hello()
torch.manual_seed(1)

print(torch.__version__)
torch.set_default_tensor_type('torch.FloatTensor')

num_inputs = 2
num_examples = 1000
true_w = [2, -2.1]
true_b = 4.9
features = torch.tensor(np.random.normal(0, 1, (num_examples, num_inputs)), dtype=torch.float)
labels = true_w[0] * features[:, 0] + true_w[1] * features[:, 1] + true_b
labels += torch.tensor(np.random.normal(0, 0.01, size=labels.size()), dtype=torch.float)  # 干扰项

# 读取数据
import torch.utils.data as Data

batch_size = 10

# 将训练数据的特征和标签组合
dataset = Data.TensorDataset(features, labels)

# 把 dataset 放入 DataLoader
data_iter = Data.DataLoader(
    dataset=dataset,  # torch TensorDataset format
    batch_size=batch_size,  # mini batch size
    shuffle=True,  # 要不要打乱数据 (打乱比较好)
    num_workers=2,  # 多线程来读数据
)

for X, y in data_iter:
    print(X, '\n', y)
    break


# TODO 定义模型
class LinearNet(nn.Module):
    def __init__(self, n_feature):
        super(LinearNet, self).__init__()
        self.linear = nn.Linear(n_feature, 1)
        # self.linear.weight = true_w
        # self.linear.bias = true_b

    def forward(self, x):
        y = self.linear(x)
        return y


net = LinearNet(num_inputs)
print(net)  # 使用print可以打印出网络的结构

# ？TODO 其他写法
# 写法一
net = nn.Sequential(
    nn.Linear(num_inputs, 1)
    # 此处还可以传入其他层
)

# 写法二
net = nn.Sequential()
net.add_module('linear', nn.Linear(num_inputs, 1))
# net.add_module ......

# 写法三
from collections import OrderedDict

net = nn.Sequential(OrderedDict([
    ('linear', nn.Linear(num_inputs, 1))
    # ......
]))

print(net)
print(net[0])

for param in net.parameters():
    print(param)

from torch.nn import init

init.normal_(net[0].weight, mean=0.0, std=0.01)
init.constant_(net[0].bias, val=0.0)  # 也可以直接修改bias的data: net[0].bias.data.fill_(0)

net = LinearNet(num_inputs)
print(type(net))
for param in net.parameters():
    print(param)

loss = nn.MSELoss()
import torch.optim as optim

optimizer = optim.SGD(net.parameters(), lr=0.03)
print(optimizer)

# 为不同子网络设置不同的学习率
# optimizer =optim.SGD([
#                 # 如果对某个参数不指定学习率，就使用最外层的默认学习率
#                 {'params': net.subnet1.parameters()}, # lr=0.03
#                 {'params': net.subnet2.parameters(), 'lr': 0.01}
#             ], lr=0.03)
# 调整学习率
# for param_group in optimizer.param_groups:
#     param_group['lr'] *= 0.1  # 学习率为之前的0.1倍

num_epochs = 10
for epoch in range(1, num_epochs + 1):
    for X, y in data_iter:
        output = net(X)
        l = loss(output, y.view(-1, 1))
        net.zero_grad()
        optimizer.zero_grad()  # 梯度清零，等价于net.zero_grad()
        l.backward()
        optimizer.step()
    print('epoch %d, loss: %f' % (epoch, l.item()))

# dense = net[0]
# print()
# print(true_w, dense.weight.data)
# print()
# print(true_b, dense.bias.data)

# TODO
print()
print(type(net.linear.weight))
print(true_w, net.linear.weight)
print()
print(true_b, net.linear.bias)
