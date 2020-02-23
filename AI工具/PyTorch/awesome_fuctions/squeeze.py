

# 原文链接：https://blog.csdn.net/sinat_40624829/article/details/91127373
# torch.squeeze(input, dim=None, out=None)
# 输出：将输入所有维度为1的去除（2，1）=（2，）（以行向量的形式存在）
#
# x = torch.zeros(2, 1, 2, 1, 2)
# x.size()
#
# torch.Size([2, 1, 2, 1, 2])
#
# y = torch.squeeze(x)
# y.size()

