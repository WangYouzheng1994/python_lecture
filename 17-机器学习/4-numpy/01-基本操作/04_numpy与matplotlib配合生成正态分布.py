import matplotlib.pyplot as plt
import numpy as np

# 从-1 到1 ，选一亿个数

x1 = np.random.uniform(-1, 1, 100000000)

# 创建画布
plt.figure(figsize=(10, 10), dpi = 100)

# x是数据量，bins划分的区间数，简单地说就是 y轴的精细度
plt.hist(x=x1, bins=10000)

plt.show()