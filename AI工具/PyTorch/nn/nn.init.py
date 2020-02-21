
# https://blog.csdn.net/weixin_42018112/article/details/90725819
import torch
import torch.nn as nn

w = torch.empty(2, 3)

# 1. 均匀分布 - u(a, b)
# torch.nn.init.uniform_(tensor, a=0, b=1)
nn.init.uniform_(w)
# tensor([[ 0.0578,  0.3402,  0.5034],
#         [ 0.7865,  0.7280,  0.6269]])

# 2. 正态分布 - N(mean, std)
# torch.nn.init.normal_(tensor, mean=0, std=1)
nn.init.normal_(w)
# tensor([[ 0.3326,  0.0171, -0.6745],
#        [ 0.1669,  0.1747,  0.0472]])

# 3. 常数 - 固定值 val
# torch.nn.init.constant_(tensor, val)
nn.init.constant_(w, 0.3)
# tensor([[ 0.3000,  0.3000,  0.3000],
#         [ 0.3000,  0.3000,  0.3000]])

#4. 对角线为1， 其它为0
# torch.nn.init.eye_(tensor)
nn.init.eye_(w)
# tensor([[ 1.,  0.,  0.],
#         [ 0.,  1.,  0.]])

# 5. Dirac delta 函数初始化，仅适用于 {3, 4, 5}-维的 torch.Tensor
# torch.nn.init.dirac_(tensor)
w1 = torch.empty(3, 16, 5, 5)
nn.init.dirac_(w1)

# 6. xavier_uniform 初始化
# torch.nn.init.xavier_uniform_(tensor, gain=1)
# From - Understanding the difficulty of training deep feedforward neural networks - Bengio 2010
nn.init.xavier_uniform_(w, gain=nn.init.calculate_gain('relu'))
# tensor([[ 1.3374,  0.7932, -0.0891],
#         [-1.3363, -0.0206, -0.9346]])

# 7. xavier_normal 初始化
# torch.nn.init.xavier_normal_(tensor, gain=1)
nn.init.xavier_normal_(w)
# tensor([[-0.1777,  0.6740,  0.1139],
#         [ 0.3018, -0.2443,  0.6824]])

# 8. kaiming_uniform 初始化
# From - Delving deep into rectifiers: Surpassing human-level performance on ImageNet classification - He Kaiming 2015
# torch.nn.init.kaiming_uniform_(tensor, a=0, mode='fan_in', nonlinearity='leaky_relu')
nn.init.kaiming_uniform_(w, mode='fan_in', nonlinearity='relu')
# tensor([[ 0.6426, -0.9582, -1.1783],
#         [-0.0515, -0.4975,  1.3237]])

# 9. kaiming_normal 初始化
# torch.nn.init.kaiming_normal_(tensor, a=0, mode='fan_in', nonlinearity='leaky_relu')
nn.init.kaiming_normal_(w, mode='fan_out', nonlinearity='relu')
# tensor([[ 0.2530, -0.4382,  1.5995],
#         [ 0.0544,  1.6392, -2.0752]])

# 10. 正交矩阵 - (semi)orthogonal matrix
# From - Exact solutions to the nonlinear dynamics of learning in deep linear neural networks - Saxe 2013
# torch.nn.init.orthogonal_(tensor, gain=1)
nn.init.orthogonal_(w)
# tensor([[ 0.5786, -0.5642, -0.5890],
#         [-0.7517, -0.0886, -0.6536]])

# 11. 稀疏矩阵 - sparse matrix
# 非零元素采用正态分布 N(0, 0.01) 初始化.
# From - Deep learning via Hessian-free optimization - Martens 2010
# torch.nn.init.sparse_(tensor, sparsity, std=0.01)
nn.init.sparse_(w, sparsity=0.1)
# tensor(1.00000e-03 *
#        [[-0.3382,  1.9501, -1.7761],
#         [ 0.0000,  0.0000,  0.0000]])
