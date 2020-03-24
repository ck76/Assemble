import torch
from torch import nn

print(torch.__version__)


class MLP(nn.Module):
    # 声明带有模型参数的层，这里声明了两个全连接层
    def __init__(self, **kwargs):
        # 调用MLP父类Block的构造函数来进行必要的初始化。这样在构造实例时还可以指定其他函数
        # 参数，如“模型参数的访问、初始化和共享”一节将介绍的模型参数params
        super(MLP, self).__init__(**kwargs)
        self.hidden = nn.Linear(784, 256)  # 隐藏层
        self.act = nn.ReLU()
        self.output = nn.Linear(256, 10)  # 输出层

    # 定义模型的前向计算，即如何根据输入x计算返回所需要的模型输出
    def forward(self, x):
        a = self.act(self.hidden(x))
        return self.output(a)

X = torch.rand(2, 784)
net = MLP()
print(net)
net(X)

# MLP(
#   (hidden): Linear(in_features=784, out_features=256, bias=True)
#   (act): ReLU()
#   (output): Linear(in_features=256, out_features=10, bias=True)
# )
# tensor([[ 0.1351, -0.0034,  0.0948, -0.1652,  0.1512,  0.0887, -0.0032,  0.0692,
#           0.0942,  0.0956],
#         [ 0.1624, -0.0383,  0.1557, -0.0735,  0.1931,  0.1699, -0.0067,  0.0353,
#           0.1712,  0.1568]], grad_fn=<ThAddmmBackward>)


class MySequential(nn.Module):
    from collections import OrderedDict
    def __init__(self, *args):
        super(MySequential, self).__init__()
        if len(args) == 1 and isinstance(args[0], OrderedDict): # 如果传入的是一个OrderedDict
            for key, module in args[0].items():
                self.add_module(key, module)  # add_module方法会将module添加进self._modules(一个OrderedDict)
        else:  # 传入的是一些Module
            for idx, module in enumerate(args):
                self.add_module(str(idx), module)
    def forward(self, input):
        # self._modules返回一个 OrderedDict，保证会按照成员添加时的顺序遍历成
        for module in self._modules.values():
            input = module(input)
        return input

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


# TODO 构造复杂的模型
class FancyMLP(nn.Module):
    def __init__(self, **kwargs):
        super(FancyMLP, self).__init__(**kwargs)

        self.rand_weight = torch.rand((20, 20), requires_grad=False)  # 不可训练参数（常数参数）
        self.linear = nn.Linear(20, 20)

    def forward(self, x):
        x = self.linear(x)
        # 使用创建的常数参数，以及nn.functional中的relu函数和mm函数
        x = nn.functional.relu(torch.mm(x, self.rand_weight.data) + 1)

        # 复用全连接层。等价于两个全连接层    共享参数
        x = self.linear(x)
        # 控制流，这里我们需要调用item函数来返回标量进行比较
        while x.norm().item() > 1:
            x /= 2
        if x.norm().item() < 0.8:
            x *= 10
        return x.sum()

X = torch.rand(2, 20)
net = FancyMLP()
print(net)
net(X)
# FancyMLP(
#   (linear): Linear(in_features=20, out_features=20, bias=True)
# )
# tensor(12.1594, grad_fn=<SumBackward0>)

class NestMLP(nn.Module):
    def __init__(self, **kwargs):
        super(NestMLP, self).__init__(**kwargs)
        self.net = nn.Sequential(nn.Linear(40, 30), nn.ReLU())

    def forward(self, x):
        return self.net(x)

net = nn.Sequential(NestMLP(), nn.Linear(30, 20), FancyMLP())

X = torch.rand(2, 40)
print(net)
net(X)
# Sequential(
#   (0): NestMLP(
#     (net): Sequential(
#       (0): Linear(in_features=40, out_features=30, bias=True)
#       (1): ReLU()
#     )
#   )
#   (1): Linear(in_features=30, out_features=20, bias=True)
#   (2): FancyMLP(
#     (linear): Linear(in_features=20, out_features=20, bias=True)
#   )
# )
# tensor(0.1509, grad_fn=<SumBackward0>)