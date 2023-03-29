import numpy as np
# 生成一个 均值为0，标准差是1的正态分布的4*5的数组
array = np.random.normal(5, 1, (4, 5))
print(array)
print(array.reshape([10, 8]))
