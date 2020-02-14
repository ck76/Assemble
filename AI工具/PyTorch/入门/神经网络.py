import torch
import torch.nn as nn
import torch.nn.functional as F

"""
# N是批大小；D是输入维度
# H是隐藏层维度；D_out是输出维度
N, D_in, H, D_out = 64, 1000, 100, 10

# 产生输入和输出随机张量
x = torch.randn(N, D_in)
y = torch.randn(N, D_out)
"""
# N是批大小；D是输入维度
# H是隐藏层维度；D_out是输出维度
N, D_in, H, D_out = 64, 1000, 100, 10

# 产生输入和输出随机张量
x = torch.randn(N, D_in)
y = torch.randn(N, D_out)


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        # 输入图像channel：1；输出channel：6；5x5卷积核
        # in_channels(int) – 输入信号的通道
        # out_channels(int) – 卷积产生的通道
        # kerner_size(int or tuple) - 卷积核的尺寸,在nlp中tuple用更多，（n,embed_size）
        # stride(int or tuple, optional) - 卷积步长
        # padding(int or tuple, optional) - 输入的每一条边补充0的层数
        # dilation(int or tuple, optional) – 卷积核元素之间的间距
        # groups(int, optional) – 从输入通道到输出通道的阻塞连接数
        # bias(bool, optional) - 如果bias=True，添加偏置
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=6, kernel_size=5)
        self.conv2 = nn.Conv2d(6, 16, 5)
        # an affine operation: y = Wx + b
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    # class torch.nn.MaxPool2d(kernel_size, stride=None, padding=0, dilation=1, return_indices=False, ceil_mode=False)
    # 如果padding不是0，会在输入的每一边添加相应数目0  比如padding=1，则在每一边分别补0 ，其实最后的结果补出来是bias
    #
    # 参数：
    #
    # kernel_size(int or tuple) - max pooling的窗口大小，可以为tuple，在nlp中tuple用更多，（n,1）
    # stride(int or tuple, optional) - max pooling的窗口移动的步长。默认值是kernel_size
    # padding(int or tuple, optional) - 输入的每一条边补充0的层数
    # dilation(int or tuple, optional) – 一个控制窗口中元素步幅的参数
    # return_indices - 如果等于True，会返回输出最大值的序号，对于上采样操作会有帮助
    # ceil_mode - 如果等于True，计算输出信号大小的时候，会使用向上取整，代替默认的向下取整的操作
    def forward(self, x):
        """
                对于模型的前向传播，我们随机选择0、1、2、3，并重用了多次计算隐藏层的middle_linear模块。
                由于每个前向传播构建一个动态计算图，
                我们可以在定义模型的前向传播时使用常规Python控制流运算符，如循环或条件语句。
                在这里，我们还看到，在定义计算图形时多次重用同一个模块是完全安全的。
                这是Lua Torch的一大改进，因为Lua Torch中每个模块只能使用一次。
                """
        # 2x2 Max pooling
        relu1 = F.relu(self.conv1(x))
        x = F.max_pool2d(input=relu1, kernel_size=(2, 2))
        relu2 = F.relu(self.conv2(x))
        # 如果是方阵,则可以只使用一个数字进行定义
        x = F.max_pool2d(relu2, 2)

        x = x.view(-1, self.num_flat_features(x))
        # 线性整流函数
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

    def num_flat_features(self, x):
        print(x.size)
        size = x.size()[1:]  # 除去批处理维度的其他所有维度
        num_features = 1
        for s in size:
            num_features *= s
        return num_features


net = Net()
print(net)
# Net(
#   (conv1): Conv2d(1, 6, kernel_size=(5, 5), stride=(1, 1))
#   (conv2): Conv2d(6, 16, kernel_size=(5, 5), stride=(1, 1))
#   (fc1): Linear(in_features=400, out_features=120, bias=True)
#   (fc2): Linear(in_features=120, out_features=84, bias=True)
#   (fc3): Linear(in_features=84, out_features=10, bias=True)
# )

params = list(net.parameters())
print(len(params))
print(params[0].size())  # conv1's .weight torch.Size([6, 1, 5, 5])

input = torch.randn(1, 1, 32, 32)
out = net(input)
print(out)

net.zero_grad()
out.backward(torch.randn(1, 10))
# 注意：
# torch.nn只支持小批量处理（mini-batches）。整个torch.nn包只支持小批量样本的输入，不支持单个样本。
# 比如，nn.Conv2d 接受一个4维的张量，即 TODO nSamples x nChannels x Height x Width
# 如果是一个单独的样本，只需要使用input.unsqueeze(0)来添加一个“假的”批大小维度。
# TODO 复习：
# torch.Tensor - 一个多维数组，支持诸如backward()等的自动求导操作，同时也保存了张量的梯度。
# nn - 神经网络模块。是一种方便封装参数的方式，具有将参数移动到GPU、导出、加载等功能。
# nn.Parameter - 张量的一种，当它作为一个属性分配给一个Module时，它会被自动注册为一个参数。
# autograd.Function - 实现了自动求导前向和反向传播的定义，每个Tensor至少创建一个Function节点，该节点连接到创建Tensor的函数并对其历史进行编码。


# TODO 损失函数
output = net(input)
target = torch.randn(10)  # 本例子中使用模拟数据
target = target.view(1, -1)  # 使目标值与数据值形状一致
criterion = nn.MSELoss()
loss = criterion(output, target)

print("loss=", loss)
# TODO 现在，如果使用loss的.grad_fn属性跟踪反向传播过程，会看到计算图如下：
# input -> conv2d -> relu -> maxpool2d -> conv2d -> relu -> maxpool2d
#       -> view -> linear -> relu -> linear -> relu -> linear
#       -> MSELoss
#       -> loss

# 所以，当我们调用loss.backward()，整张图开始关于loss微分，图中所有设置了requires_grad=True的张量的.grad属性累积着梯度张量。
print()
net.zero_grad()  # 清零所有参数（parameter）的梯度缓存
print('conv1.bias.grad before backward')
print(net.conv1.bias.grad)

loss.backward()

print('conv1.bias.grad after backward')
print(net.conv1.bias.grad)

# TODO 更新权重
# 最简单的更新规则是随机梯度下降法（SGD）:
# weight = weight - learning_rate * gradient
learning_rate = 0.01
for f in net.parameters():
    f.data.sub_(f.grad.data * learning_rate)

import torch.optim as optim

# 创建优化器（optimizer）
optimizer = optim.SGD(net.parameters(), lr=0.01)

# 在训练的迭代中：
optimizer.zero_grad()  # 清零梯度缓存
output = net(input)
loss = criterion(output, target)
loss.backward()
optimizer.step()  # 更新参数

# for t in range(500):
#     # 前向传播：通过向模型传递x计算预测值y
#     y_pred = net(x)
#
#     # 计算并输出loss
#     loss = criterion(y_pred, y)
#     if t % 100 == 99:
#         print(t, loss.item())
#
#     # 清零梯度，反向传播，更新权重
#     optimizer.zero_grad()
#     loss.backward()
#     optimizer.step()

# TODO 卷积神经网络CNN的结构一般包含这几层：
#
# TODO    输入层：用于数据的输入
#
# TODO    卷积层：使用卷积核进行特征提取和特征映射
#
# TODO   激励层：由于卷积也是一种线性运算，因此需要增加非线性映射
#
# TODO  池化层：进行下采样，对特征图稀疏处理，减少特征信息的损失
#
# TODO  输出层：用于输出结果
class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        # 26.定义①的卷积层，输入为32x32的图像，卷积核大小5x5卷积核种类6
        self.conv1 = nn.Conv2d(3, 6, 5)
        # 27.定义③的卷积层，输入为前一层6个特征，卷积核大小5x5，卷积核种类16
        self.conv2 = nn.Conv2d(6, 16, 5)
        # 28.定义⑤的全链接层，输入为16*5*5，输出为120
        self.fc1 = nn.Linear(16 * 5 * 5, 120)  # 6*6 from image dimension
        # 29.定义⑥的全连接层，输入为120，输出为84
        self.fc2 = nn.Linear(120, 84)
        # 30.定义⑥的全连接层，输入为84，输出为10
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        # 31.完成input-S2，先卷积+relu，再2x2下采样
        x = F.max_pool2d(F.relu(self.conv1(x)), (2, 2))
        # 32.完成S2-S4，先卷积+relu，再2x2下采样
        x = F.max_pool2d(F.relu(self.conv2(x)), 2) #卷积核方形时，可以只写一个维度
        # 33.将特征向量扁平成行向量
        x = x.view(-1, 16 * 5 * 5)
        # 34.使用fc1+relu
        x = F.relu(self.fc1(x))
        # 35.使用fc2+relu
        x = F.relu(self.fc2(x))
        # 36.使用fc3
        x = self.fc3(x)
        return x


net = Net()
print(net)
print(net.state_dict())