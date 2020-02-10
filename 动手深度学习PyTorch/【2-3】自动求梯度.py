import torch

x = torch.zeros(2, 2, requires_grad=True)
print(x)
print(x.grad_fn)

y = x + 2
print(y)
print(y.grad_fn)

print(x.is_leaf, y.is_leaf)

z = y * y + 3
out = z.mean()
print(z)
print(out)

out.backward()
print(x.grad)
# 􏲚􏵤􏲛grad􏱀􏵙􏱕􏲥􏵈􏲸􏵖􏱊􏳁􏵢􏵿􏰐(accumulated)􏰖􏰮􏵤􏶒􏶓􏱙􏰆􏴢􏵉􏰹􏵙􏱕􏲥􏵈􏰖􏴨􏱔􏴭􏲽􏵢 􏵿􏲟􏵕􏰐􏴨􏱔􏰖􏰢􏲍􏰆􏶔􏱀􏵙􏱕􏲥􏵈􏲟􏵕􏰣􏶕􏴨􏱔􏶖􏱄􏰓梯度在每一次传播都是累加的，新计算梯度的时候清空之前的梯度
# out2 = z.mean()
# out2.backward()
# print(x.grad)
#
# out3 = z.mean()
# z.grad.data.zero_()
# out3.backward()
# print(x.grad)

a=torch.zeros(2,3)
b=torch.ones(2,3)
print(a*b)
print(b.sum())