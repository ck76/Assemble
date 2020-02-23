

# TODO 如果我们有两个tensor是A和B，想把他们拼接在一起，需要如下操作
#  https://www.cnblogs.com/JeasonIsCoding/p/10162356.html
# C = torch.cat( (A,B),0 )  #按维数0拼接（竖着拼）
#
# C = torch.cat( (A,B),1 )  #按维数1拼接（横着拼）

# >>> import torch
# >>> A=torch.ones(2,3)    #2x3的张量（矩阵）
# >>> A
# tensor([[ 1.,  1.,  1.],
#         [ 1.,  1.,  1.]])
# >>> B=2*torch.ones(4,3)  #4x3的张量（矩阵）
# >>> B
# tensor([[ 2.,  2.,  2.],
#         [ 2.,  2.,  2.],
#         [ 2.,  2.,  2.],
#         [ 2.,  2.,  2.]])
# >>> C=torch.cat((A,B),0)  #按维数0（行）拼接
# >>> C
# tensor([[ 1.,  1.,  1.],
#          [ 1.,  1.,  1.],
#          [ 2.,  2.,  2.],
#          [ 2.,  2.,  2.],
#          [ 2.,  2.,  2.],
#          [ 2.,  2.,  2.]])
# >>> C.size()
# torch.Size([6, 3])
# >>> D=2*torch.ones(2,4) #2x4的张量（矩阵）
# >>> C=torch.cat((A,D),1)#按维数1（列）拼接
# >>> C
# tensor([[ 1.,  1.,  1.,  2.,  2.,  2.,  2.],
#         [ 1.,  1.,  1.,  2.,  2.,  2.,  2.]])
# >>> C.size()
# torch.Size([2, 7])