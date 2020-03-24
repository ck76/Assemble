import torch
from torch import nn
#
"""
!nvidia-smi # 对Linux/macOS用户有效
Sun Mar 17 16:12:15 2019       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 390.48                 Driver Version: 390.48                    |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|===============================+======================+======================|
|   0  GeForce GTX 1050    Off  | 00000000:01:00.0 Off |                  N/A |
| 20%   40C    P5    N/A /  75W |   1213MiB /  2000MiB |     23%      Default |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                       GPU Memory |
|  GPU       PID   Type   Process name                             Usage      |
|=============================================================================|
|    0      1235      G   /usr/lib/xorg/Xorg                           434MiB |
|    0      2095      G   compiz                                       171MiB |
|    0      2660      G   /opt/teamviewer/tv_bin/TeamViewer              5MiB |
|    0      4166      G   /proc/self/exe                               397MiB |
|    0     13274      C   /home/tss/anaconda3/bin/python               191MiB |
+-----------------------------------------------------------------------------+"""
print(torch.cuda.is_available()) # cuda是否可用
# print(torch.cuda.device_count() )# gpu数量
# print(torch.cuda.current_device())
# print(torch.cuda.get_device_name(0))

x = torch.tensor([1, 2, 3])
x = x.cuda(0)
print(x)


# Tensor的GPU计算
x = torch.tensor([1, 2, 3])
# tensor([1, 2, 3])

x = x.cuda(0)
# tensor([1, 2, 3], device='cuda:0')

x.device
# device(type='cuda', index=0)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
x = torch.tensor([1, 2, 3], device=device)
# or
x = torch.tensor([1, 2, 3]).to(device)
# tensor([1, 2, 3], device='cuda:0')
y = x**2
# tensor([1, 4, 9], device='cuda:0')
# z = y + x.cpu()


# 型的GPU计算
net = nn.Linear(3, 1)
list(net.parameters())[0].device
# device(type='cpu')

net.cuda()
list(net.parameters())[0].device
# device(type='cuda', index=0)


x = torch.rand(2,3).cuda()
net(x)
# tensor([[-0.5574],
#         [-0.3792]], device='cuda:0', grad_fn=<ThAddmmBackward>)