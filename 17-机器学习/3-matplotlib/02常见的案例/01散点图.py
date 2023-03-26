import random
import matplotlib.pyplot as plt

x = range(50)
# 数值
x = [random.uniform(5, 200) for i in x]
y2 = [random.uniform(5, 200) for i in x]

# 1. 创建画布
plt.figure(figsize=(20, 8), dpi=100)
# 2. 绘制图像
plt.scatter(x, y2)

# 3. 图像展示
plt.show()