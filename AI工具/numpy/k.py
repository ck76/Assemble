import numpy as np
import torch

ck = np.arange(0, 12).reshape(-1, 3)
print(ck, ck.shape)
ckkk = torch.from_numpy(ck)
print(ckkk.sum(dim=0))
print(ckkk.sum(dim=1))
