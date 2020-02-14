import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from mpl_toolkits.mplot3d import Axes3D

t=np.arange(0.0,2.0,0.1)
s=np.sin(t*np.pi)
plt.subplot(2,2,1) #要生成两行两列，这是第一个图plt.subplot('行','列','编号')
plt.plot(t,s,'b--')
plt.ylabel('y1')
plt.subplot(2,2,2) #两行两列,这是第二个图
plt.plot(2*t,s,'r--')
plt.ylabel('y2')
plt.subplot(2,2,3)#两行两列,这是第三个图
plt.plot(3*t,s,'m--')
plt.subplot(2,2,4)#两行两列,这是第四个图
plt.plot(4*t,s,'k--')
plt.show()
