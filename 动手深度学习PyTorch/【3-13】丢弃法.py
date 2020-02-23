import torch
import torch.nn as nn
import numpy as np
import sys
import d2lzh_pytorch as d2l

print(torch.__version__)


# TODO drop_prob:丢弃概率
def dropout(X, drop_prob):
    X = X.float()
    assert 0 <= drop_prob <= 1
    keep_prob = 1 - drop_prob
    # 这种情况下把全部元素都丢弃
    if keep_prob == 0:
        return torch.zeros_like(X)
    mask = (torch.randn(X.shape) < keep_prob).float()

    return mask * X / keep_prob


X = torch.arange(16).view(2, 8)
dropout(X, 0)
# tensor([[ 0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.],
#         [ 8.,  9., 10., 11., 12.,  0., 14., 15.]])

dropout(X, 0.5)
# tensor([[ 0.,  0.,  4.,  0.,  8.,  0., 12., 14.],
#         [ 0., 18., 20.,  0., 24.,  0.,  0., 30.]])

dropout(X, 1.0)
# tensor([[0., 0., 0., 0., 0., 0., 0., 0.],
#         [0., 0., 0., 0., 0., 0., 0., 0.]])

num_inputs, num_outputs, num_hiddens1, num_hiddens2 = 784, 10, 256, 256

W1 = torch.tensor(np.random.normal(0, 0.01, size=(num_inputs, num_hiddens1)), dtype=torch.float, requires_grad=True)
b1 = torch.zeros(num_hiddens1, requires_grad=True)
W2 = torch.tensor(np.random.normal(0, 0.01, size=(num_hiddens1, num_hiddens2)), dtype=torch.float, requires_grad=True)
b2 = torch.zeros(num_hiddens2, requires_grad=True)
W3 = torch.tensor(np.random.normal(0, 0.01, size=(num_hiddens2, num_outputs)), dtype=torch.float, requires_grad=True)
b3 = torch.zeros(num_outputs, requires_grad=True)

params = [W1, b1, W2, b2, W3, b3]

drop_prob1, drop_prob2 = 0.2, 0.5


def net(X, is_training=True):
    X = X.view(-1, num_inputs)
    H1 = (torch.matmul(X, W1) + b1).relu()
    if is_training:  # 只在训练模型时使用丢弃法
        H1 = dropout(H1, drop_prob1)  # 在第一层全连接后添加丢弃层
    H2 = (torch.matmul(H1, W2) + b2).relu()
    if is_training:
        H2 = dropout(H2, drop_prob2)  # 在第二层全连接后添加丢弃层
    return torch.matmul(H2, W3) + b3


# def evaluate_accuracy(data_iter, net):
#     acc_sum, n = 0.0, 0
#     for X, y in data_iter:
#         if isinstance(net, torch.nn.Module):
#             net.eval() # 评估模式, 这会关闭dropout
#             acc_sum += (net(X).argmax(dim=1) == y).float().sum().item()
#             net.train() # 改回训练模式
#         else: # 自定义的模型
#             if('is_training' in net.__code__.co_varnames): # 如果有is_training这个参数
#                 # 将is_training设置成False
#                 acc_sum += (net(X, is_training=False).argmax(dim=1) == y).float().sum().item()
#             else:
#                 acc_sum += (net(X).argmax(dim=1) == y).float().sum().item()
#         n += y.shape[0]
#     return acc_sum / n


num_epochs, lr, batch_size = 5, 100.0, 256  # 这里的学习率设置的很大，原因同3.9.6节。
loss = torch.nn.CrossEntropyLoss()
train_iter, test_iter = d2l.load_data_fashion_mnist(batch_size)
d2l.train_ch3(net, train_iter, test_iter, loss, num_epochs, batch_size, params, lr)

# epoch 1, loss 0.0044, train acc 0.574, test acc 0.648
# epoch 2, loss 0.0023, train acc 0.786, test acc 0.786
# epoch 3, loss 0.0019, train acc 0.826, test acc 0.825
# epoch 4, loss 0.0017, train acc 0.839, test acc 0.831
# epoch 5, loss 0.0016, train acc 0.849, test acc 0.850

# TODO 简洁实现
net = nn.Sequential(
    d2l.FlattenLayer(),
    nn.Linear(num_inputs, num_hiddens1),
    nn.ReLU(),
    nn.Dropout(drop_prob1),
    nn.Linear(num_hiddens1, num_hiddens2),
    nn.ReLU(),
    nn.Dropout(drop_prob2),
    nn.Linear(num_hiddens2, 10)
)

for param in net.parameters():
    nn.init.normal_(param, mean=0, std=0.01)

optimizer = torch.optim.SGD(net.parameters(), lr=0.5)
d2l.train_ch3(net, train_iter, test_iter, loss, num_epochs, batch_size, None, None, optimizer)
