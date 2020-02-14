import torch
import torchvision
import numpy as np
import sys
import d2lzh_pytorch as d2l

print(torch.__version__)
print(torchvision.__version__)

batch_size = 256
train_iter, test_iter = d2l.load_data_fashion_mnist(batch_size, root='~/Datasets')

# 初始化模型参数
# TODO 28*28*1=784
num_inputs = 784
num_outputs = 10

W = torch.tensor(np.random.normal(0, 0.01, (num_inputs, num_outputs)), dtype=torch.float)
b = torch.zeros(num_outputs, dtype=torch.float)
W.requires_grad_(requires_grad=True)
b.requires_grad_(requires_grad=True)

X = torch.tensor([[1, 2, 3], [4, 5, 6]])
# 保持输出的维度 。当keepdim=False时，输出比输入少一个维度（就是指定的dim求范数的维度）。而
# keepdim=True时，输出与输入维度相同，仅仅是输出在求范数的维度上元素个数变为1。这也是为什么有时
# 我们把参数中的dim称为缩减的维度，因为norm运算之后，此维度或者消失或者元素个数变为1。
print(X.sum(dim=0, keepdim=True))
print(X.sum(dim=1, keepdim=True))
print(X.sum(dim=0, keepdim=True).shape)
print(X.sum(dim=0, keepdim=False).shape)


# TODO 实现softmax运算
def softmax(X):
    X_exp = X.exp()
    partition = X_exp.sum(dim=1, keepdim=True)
    return X_exp / partition  # 这里应用了广播机制


X = torch.rand((2, 5))
X_prob = softmax(X)
print(X_prob, X_prob.sum(dim=1))  # 都在和为1


#  定义模型
def net(X):
    # torch.mul(a, b)是矩阵a和b对应位相乘，a和b的维度必须相等，比如a的维度是(1, 2)，b的维度是(1, 2)，返回的仍是(1, 2)的矩阵
    # torch.mm(a, b)是矩阵a和b矩阵相乘，比如a的维度是(1, 2)，b的维度是(2, 3)，返回的就是(1, 3)的矩阵
    print(X.view(-1, num_inputs).shape)
    return softmax(torch.mm(X.view(-1, num_inputs), W) + b)


# TODO https://www.jianshu.com/p/5d1f8cd5fe31 gather
# 函数torch.gather(input, dim, index, out=None) → Tensor
# 沿给定轴 dim ,将输入索引张量 index 指定位置的值进行聚合.
# input (Tensor) – 源张量
# dim (int) – 索引的轴
# index (LongTensor) – 聚合元素的下标(index需要是torch.longTensor类型)
# out (Tensor, optional) – 目标张量
y_hat = torch.tensor([[0.1, 0.3, 0.6], [0.3, 0.2, 0.5]])
print(y_hat)
y = torch.LongTensor([0, 2])
print(torch.gather(y_hat, 1, y.view(-1, 1)))


def cross_entropy(y_hat, y):
    return - torch.log(y_hat.gather(1, y.view(-1, 1)))


def accuracy(y_hat, y):
    # argmax 返回指定维度最大值的序号
    print(y_hat.shape)
    print(y_hat)
    print(y_hat.argmax(dim=0))
    print(y_hat.argmax(dim=1))
    print(type((y_hat.argmax(dim=1) == y)), (y_hat.argmax(dim=1) == y))
    #   item是得到一个元素张量里面的元素值
    # pytorch中的.item()用于将一个零维张量转换成浮点数
    return (y_hat.argmax(dim=1) == y).float().mean().item()


print(accuracy(y_hat, y))


def evaluate_accuracy(data_iter, net):
    acc_sum, n = 0.0, 0
    for X, y in data_iter:
        acc_sum += (net(X).argmax(dim=1) == y).float().sum().item()
        n += y.shape[0]
    return acc_sum / n


print(evaluate_accuracy(test_iter, net))

# TODO 训练模型
num_epochs, lr = 2, 0.1


# 本函数已保存在d2lzh_pytorch包中方便以后使用
def train_ch3(net, train_iter, test_iter, loss, num_epochs, batch_size,
              params=None, lr=None, optimizer=None):
    for epoch in range(num_epochs):
        train_l_sum, train_acc_sum, n = 0.0, 0.0, 0
        for X, y in train_iter:
            y_hat = net(X)
            l = loss(y_hat, y).sum()

            # 梯度清零
            if optimizer is not None:
                optimizer.zero_grad()
            elif params is not None and params[0].grad is not None:
                for param in params:
                    param.grad.data.zero_()

            l.backward()
            if optimizer is None:
                d2l.sgd(params, lr, batch_size)
            else:
                optimizer.step()  # “softmax回归的简洁实现”一节将用到

            train_l_sum += l.item()
            train_acc_sum += (y_hat.argmax(dim=1) == y).sum().item()
            n += y.shape[0]
        test_acc = evaluate_accuracy(test_iter, net)
        print('epoch %d, loss %.4f, train acc %.3f, test acc %.3f'
              % (epoch + 1, train_l_sum / n, train_acc_sum / n, test_acc))


train_ch3(net, train_iter, test_iter, cross_entropy, num_epochs, batch_size, [W, b], lr)

X, y = iter(test_iter).next()
print(X.shape, y.shape)
print(net(X).shape)

true_labels = d2l.get_fashion_mnist_labels(y.numpy())
pred_labels = d2l.get_fashion_mnist_labels(net(X).argmax(dim=1).numpy())
titles = [true + '\n' + pred for true, pred in zip(true_labels, pred_labels)]

d2l.show_fashion_mnist(X[0:9], titles[0:9])
