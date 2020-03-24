import torch
from torch import nn

print(torch.__version__)
x = torch.ones(3)
torch.save(x, './x.pt')
x2 = torch.load('x.pt')
x2
y = torch.zeros(4)
torch.save([x, y], 'xy.pt')
xy_list = torch.load('xy.pt')
xy_list
torch.save({'x': x, 'y': y}, 'xy_dict.pt')
xy = torch.load('xy_dict.pt')
xy

# TODO 读写模型
class MLP(nn.Module):
    def __init__(self):
        super(MLP, self).__init__()
        self.hidden = nn.Linear(3, 2)
        self.act = nn.ReLU()
        self.output = nn.Linear(2, 1)

    def forward(self, x):
        a = self.act(self.hidden(x))
        return self.output(a)

net = MLP()
print(net.state_dict())
"""
OrderedDict([('hidden.weight', tensor([[ 0.1836, -0.1812, -0.1681],
                      [ 0.0406,  0.3061,  0.4599]])),
             ('hidden.bias', tensor([-0.3384,  0.1910])),
             ('output.weight', tensor([[0.0380, 0.4919]])),
             ('output.bias', tensor([0.1451]))])
             """

optimizer = torch.optim.SGD(net.parameters(), lr=0.001, momentum=0.9)
print(optimizer.state_dict())
"""
{'param_groups': [{'dampening': 0,
   'lr': 0.001,
   'momentum': 0.9,
   'nesterov': False,
   'params': [4624483024, 4624484608, 4624484680, 4624484752],
   'weight_decay': 0}],
 'state': {}}
 """


# X = torch.randn(2, 3)
# Y = net(X)
#
# PATH = "./net.pt"
# torch.save(net.state_dict(), PATH)
#
# net2 = MLP()
# net2.load_state_dict(torch.load(PATH))
# Y2 = net2(X)
# Y2 == Y