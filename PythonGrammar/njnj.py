"""
一个简单两层神经网络回归模型
"""
import numpy as np

# batch size
N = 32
# 输入维度
D = 100
# 隐含层单元数
H = 200
# 输出维度
O = 10

# 训练样本（这里随机生成）
X = np.random.randn(N, D)
y = np.random.randn(N, O)

# 初始化参数
W1 = np.random.randn(D, H)
b1 = np.zeros((H,))
W2 = np.random.randn(H, O)
b2 = np.zeros((O,))
print(b2)
# 训练参数
learning_rate = 1e-02
iterations = 200

# 训练过程
for t in range(iterations):
    # 前向过程
    h = X.dot(W1) + b1
    h_relu = np.maximum(h, 0)
    pred = h_relu.dot(W2) + b2

    # 定义loss，采用均方差
    loss = np.sum(np.square(y - pred))
    print("Iteration %d loss: %f" % (t, loss))

    # 反向过程计算梯度
    dpred = 2.0 * (pred - y)
    db2 = np.sum(dpred, axis=0)
    dW2 = h_relu.T.dot(db2)
    dh_relu = db2.dot(W2.T)
    dh = (h > 0) * dh_relu
    db1 = np.sum(dh, axis=0)
    dW1 = X.T.dot(dh)

    # SGD更新梯度
    params = [W1, b1, W2, b2]
    grads = [dW1, db1, dW2, db2]
    for p, g in zip(params, grads):
        p += -learning_rate * g



# ‘’‘
# 前向传播
# ’‘’
w = np.random.randn(2, 3)
x = np.random.randn(3, 5)
y = w.dot(x)

# ‘’‘
# 反向传播
# ’‘’
dy = np.random.randn(*y.shape())
dw = dy.dot(x.T)
dx = w.T.dot(dy)