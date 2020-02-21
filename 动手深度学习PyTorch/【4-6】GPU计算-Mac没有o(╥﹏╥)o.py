import torch
from torch import nn

print(torch.cuda.is_available()) # cuda是否可用
# print(torch.cuda.device_count() )# gpu数量
# print(torch.cuda.current_device())
# print(torch.cuda.get_device_name(0))

x = torch.tensor([1, 2, 3])
x = x.cuda(0)
print(x)