
# https://blog.csdn.net/qq_27825451/article/details/95888267
"""
前言：pytorch的模块Module类有很多的方法，前面的文章中已经介绍了四个常用的方法，
这四个方法可以用于获取模块中所定义的对象（即每一个层）他们分别是children()、named_children()、modules()、named_modules()方法，
本文介绍另外两个重要的方法，这两个方法会获取到模型中训练的参数（权值矩阵、偏置bias），这两个方法是model.state_dict()方法和model.parameters()方法。前面的文章参考：
pytorch教程之nn.Module类详解——使用Module类来自定义模型 https://blog.csdn.net/qq_27825451/article/details/90550890
"""
import torch
import torch.nn.functional as F
from torch.optim import SGD


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


model = MyNet()  # 构造模型

"""pytorch 中的 state_dict 是一个简单的python的字典对象,将每一层与它的对应参数建立映射关系.(如model的每一层的weights及偏置等等)

注意：

（1）只有那些参数可以训练的layer才会被保存到模型的state_dict中,如卷积层,线性层等等，像什么池化层、BN层这些本身没有参数的层是没有在这个字典中的；

（2）这个方法的作用一方面是方便查看某一个层的权值和偏置数据，另一方面更多的是在模型保存的时候使用。
"""
print(type(model.state_dict()))  # 查看state_dict所返回的类型，是一个“顺序字典OrderedDict”

for param_tensor in model.state_dict():  # 字典的遍历默认是遍历 key，所以param_tensor实际上是键值
    print(param_tensor, '\t', model.state_dict()[param_tensor].size())

'''
conv1.weight     torch.Size([32, 3, 3, 3])
conv1.bias       torch.Size([32])
conv2.weight     torch.Size([32, 3, 3, 3])
conv2.bias       torch.Size([32])
dense1.weight    torch.Size([128, 288])
dense1.bias      torch.Size([128])
dense2.weight    torch.Size([10, 128])
dense2.bias      torch.Size([10])
'''

print(type(model.parameters()))  # 返回的是一个generator

for para in model.parameters():
    print(para.size())  # 只查看形状
'''
torch.Size([32, 3, 3, 3])
torch.Size([32])
torch.Size([32, 3, 3, 3])
torch.Size([32])
torch.Size([128, 288])
torch.Size([128])
torch.Size([10, 128])
torch.Size([10])
'''

print(type(model.named_parameters()))  # 返回的是一个generator

for para in model.named_parameters():  # 返回的每一个元素是一个元组 tuple
    '''
    是一个元组 tuple ,元组的第一个元素是参数所对应的名称，第二个元素就是对应的参数值
    '''
    print(para[0], '\t', para[1].size())

'''
conv1.weight     torch.Size([32, 3, 3, 3])
conv1.bias       torch.Size([32])
conv2.weight     torch.Size([32, 3, 3, 3])
conv2.bias       torch.Size([32])
dense1.weight    torch.Size([128, 288])
dense1.bias      torch.Size([128])
dense2.weight    torch.Size([10, 128])
dense2.bias      torch.Size([10])
'''