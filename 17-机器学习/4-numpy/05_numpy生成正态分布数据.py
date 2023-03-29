import numpy as np
import matplotlib.pyplot as plt

# 生成一个正态分布的数据因此他一定会产出一个服从正态分布的数据集，loc是正态分布的均值，对应着正态分布的中心区间
# scale 正态分布的标准差，标准差越大，曲线约矮胖，标准差越小 曲线越高瘦
# size 个数
x = np.random.normal(2.75, 2.75, 1000)
# x = np.random.normal(2.75, 0, 1000)
print(x)
plt.figure(figsize=(20, 8), dpi=100)
plt.hist(x, bins=100) # bins 表示直方图x中点位的个数
plt.show()

#
# import sys
# print(sys.path)
