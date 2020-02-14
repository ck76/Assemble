"""
现在我们有一个用PyTorch构建的通用数据管道和训练循环可以用来训练很多类型的模型。 想要知道训练一个模型有多么简单，可以参照mnist_sample这个例子。

当然了，你可能还想要在模型中加入很多其它的东西，比如数据扩充，超参数调整，训练监控，迁移学习等。这些特性可以在fastai库中获取到，该库使用与本教程中介绍的相同设计方法开发的，为想要扩展模型的学习者提供了合理的后续步骤。

在教程的开始部分，我们说了要通过例子对torch.nn，torch.optim，Dataset和DataLoader进行说明。 现在我们来总结一下，我们都讲了些什么：

torch.nn
Module：创建一个可调用的，其表现类似于函数，但又可以包含状态（比如神经网络层的权重）的对象。该对象知道它包含的Parameter（s），并可以将梯度置为0，以及对梯度进行循环以更新权重等。
Parameter：是一个对张量的封装，它告诉Module在反向传播阶段更新权重。只有设置了requires_grad属性的张量会被更新。
functional：一个包含了梯度函数、损失函数等以及一些无状态的层，如卷积层和线性层的模块（通常使用F作为导入的别名）。
torch.optim：包含了优化器，比如在反向阶段更新Parameter中权重的SGD。
Dataset：一个抽象接口，包含了__len__和__getitem__，还包含了PyTorch提供的类，如TensorDataset。
DataLoader：接受任意的Dataset并生成一个可以批量返回数据的迭代器（iterator ）。
"""

# https://pytorch.apachecn.org/docs/1.2/beginner/nn_tutorial.html