import torch
from torch import nn
from torch.nn import init

print(torch.__version__)

net = nn.Sequential(nn.Linear(4, 3), nn.ReLU(), nn.Linear(3, 1))  # pytorch已进行默认初始化

print(net)
X = torch.rand(2, 4)
Y = net(X).sum()
# Sequential(
#   (0): Linear(in_features=4, out_features=3, bias=True)
#   (1): ReLU()
#   (2): Linear(in_features=3, out_features=1, bias=True)
# )
print(type(net.named_parameters()))
for name, param in net.named_parameters():
    print(name, param.size())
# <class 'generator'>
# 0.weight torch.Size([3, 4])
# 0.bias torch.Size([3])
# 2.weight torch.Size([1, 3])
# 2.bias torch.Size([1])

for name, param in net[0].named_parameters():
    print(name, param.size(), type(param))


# weight torch.Size([3, 4]) <class 'torch.nn.parameter.Parameter'>
# bias torch.Size([3]) <class 'torch.nn.parameter.Parameter'>

class MyModel(nn.Module):
    def __init__(self, **kwargs):
        super(MyModel, self).__init__(**kwargs)
        self.weight1 = nn.Parameter(torch.rand(20, 20))
        self.weight2 = torch.rand(20, 20)

    def forward(self, x):
        pass


n = MyModel()
for name, param in n.named_parameters():
    print(name)  # weight1

# ?TODO 访问模型参数
weight_0 = list(net[0].parameters())[0]
print(weight_0.data)
print(weight_0.grad)
Y.backward()
print(weight_0.grad)

# tensor([[ 0.2719, -0.0898, -0.2462,  0.0655],
#         [-0.4669, -0.2703,  0.3230,  0.2067],
#         [-0.2708,  0.1171, -0.0995,  0.3913]])
# None
# tensor([[-0.2281, -0.0653, -0.1646, -0.2569],
#         [-0.1916, -0.0549, -0.1382, -0.2158],
#         [ 0.0000,  0.0000,  0.0000,  0.0000]])
# ?TODO 初始化模型参数
for name, param in net.named_parameters():
    if 'weight' in name:
        init.normal_(param, mean=0, std=0.01)
        print(name, param.data)
#
# 0.weight tensor([[ 0.0030,  0.0094,  0.0070, -0.0010],
#         [ 0.0001,  0.0039,  0.0105, -0.0126],
#         [ 0.0105, -0.0135, -0.0047, -0.0006]])
# 2.weight tensor([[-0.0074,  0.0051,  0.0066]])

for name, param in net.named_parameters():
    if 'bias' in name:
        init.constant_(param, val=0)
        print(name, param.data)


# 0.bias tensor([0., 0., 0.])
# 2.bias tensor([0.])


# ?TODO 自定义初始化方法
def init_weight_(tensor):
    with torch.no_grad():
        tensor.uniform_(-10, 10)
        tensor *= (tensor.abs() >= 5).float()


for name, param in net.named_parameters():
    if 'weight' in name:
        init_weight_(param)
        print(name, param.data)

# 0.weight tensor([[ 7.0403,  0.0000, -9.4569,  7.0111],
#         [-0.0000, -0.0000,  0.0000,  0.0000],
#         [ 9.8063, -0.0000,  0.0000, -9.7993]])
# 2.weight tensor([[-5.8198,  7.7558, -5.0293]])

for name, param in net.named_parameters():
    if 'bias' in name:
        param.data += 1
        print(name, param.data)
# 0.bias tensor([1., 1., 1.])
# 2.bias tensor([1.])

# ?TODO 共享模型参数
linear = nn.Linear(1, 1, bias=False)
net = nn.Sequential(linear, linear)
print(net)
for name, param in net.named_parameters():
    init.constant_(param, val=3)
    print(name, param.data)
# Sequential(
#   (0): Linear(in_features=1, out_features=1, bias=False)
#   (1): Linear(in_features=1, out_features=1, bias=False)
# )
# 0.weight tensor([[3.]])

print(id(net[0]) == id(net[1]))
print(id(net[0].weight) == id(net[1].weight))
True
True

x = torch.ones(1, 1)
y = net(x).sum()
print(y)
y.backward()
print(net[0].weight.grad)
# tensor(9., grad_fn=<SumBackward0>)
# tensor([[6.]])
