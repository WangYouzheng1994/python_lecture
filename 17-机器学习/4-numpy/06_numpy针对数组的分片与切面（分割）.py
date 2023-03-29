import numpy as np

# 得到一个从0到9的一维数组
arrage = np.arange(10)
print(arrage)
print(type(arrage))

# 截取 ---- START
# 内置函数slice定义切割的索引，从0开始
s = slice(0, 2)
s1 = slice(1, 2)
print(arrage[s])
print(arrage[s1])

s_ = arrage[0:2]
print(s_)

# 得到一个二维数组
stock_range = np.random.normal(1, 100, (8, 8))
print(f'stock_range: {stock_range}')

# 这个表示，把第一行数组拿出来，然后截取第二、三元素出来
print(f'stock_range[0, 1:3]: {stock_range[0, 1:3]}')
# 这个表示，把第二行数组拿出来，然后截取第二、3个元素出来
print(f'stock_range[1, 1:3]: {stock_range[1, 1:3]}')
# 这个表示把第二行到第4行拿出来，然后每行的第二个第三个元素拿出来
print(f'stock_range[1:5, 1:3]: {stock_range[1:5, 1:3]}')

# 截取 ---- END

# 高维度数组的切割或者提取
# 生成一个三维数组
sanwei = np.array([
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[8, 9, 10], [11, 12, 13], [14, 15, 16]]
  ]
)
# 第1行的第二个的第三个 掌握好这个切分的语法~ 从上往下一层一层的拿的是用逗号分割的， 用冒号分割的表示索引的切分
print(sanwei[0, 1, 2])
