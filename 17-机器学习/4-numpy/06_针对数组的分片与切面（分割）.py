import numpy as np

# 得到一个从0到9的一维数组
arrage = np.arange(10)
print(arrage)
print(type(arrage))

# 内置函数slice定义切割的索引，从0开始
s = slice(0, 2)
s1 = slice(1, 2)
print(arrage[s])
print(arrage[s1])
