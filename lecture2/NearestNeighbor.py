import numpy as np

# 最邻近分类器（用例子学习 PyTorch==1时）
# 可能出现一圈绿色包裹着一颗黄色的情况，由此出现了k-邻近算法，通过不断改变k的值，
# https://blog.csdn.net/nineship/article/details/88245028
#  1）算距离：给定测试对象，计算它与训练集中的每个对象的距离
#  2）找邻居：圈定距离最近的k个训练对象，作为测试对象的近邻
#  3）做分类：根据这k个近邻归属的主要类别，来对测试对象分类
# 从kNN的算法描述中可以发现，有三个元素很重要，分别是距离度量，k的大小和分类规则，这便是kNN模型的三要素。
import numpy as np

class NearestNeighbor(object):
  def __init__(self):
    pass

  def train(self, X, y):
    """ X is N x D where each row is an example. Y is 1-dimension of size N """
    # the nearest neighbor classifier simply remembers all the training data
    self.Xtr = X
    self.ytr = y

  def predict(self, X):
    """ X is N x D where each row is an example we wish to predict label for """
    num_test = X.shape[0]
    # lets make sure that the output type matches the input type
    Ypred = np.zeros(num_test, dtype = self.ytr.dtype)

    # loop over all test rows
    # for i in xrange(num_test):
    for i in range(num_test):
      # find the nearest training image to the i'th test image
      # using the L1 distance (sum of absolute value differences)
      distances = np.sum(np.abs(self.Xtr - X[i,:]), axis = 1)
      min_index = np.argmin(distances) # get the index with smallest distance
      Ypred[i] = self.ytr[min_index] # predict the label of the nearest example

    return Ypred

#  Q: With N examples, how fast are training and prediction?
# A: Train O(1), predict O(N)
# his is bad: we want classifiers that are fast at prediction; slow for training is ok
