import numpy as np

# 创建adarray，定义一个二维数组：两行五列。
score = np.array(
    [
        [1, 2, 3, 4, 5, 6],
        [1, 2, 3, 4, 5, 6]
    ]
)

print(score)
print(score[0][1])  # 第一行第二列
print(score[0][4])  # 第一行第5列

# ---- 查看ndarray常见的api
# 转元祖
print(score.shape)
print(type(score.shape))

# 获取维度
print(score.ndim)

# 获取元素个数
print(score.size)

# 获取每一个元素分别所占空间的大小 字节数，因为都是同一类型的 所以所有元素空间是一样的
print(score.itemsize)  # 4  4字节
# 获取元素类型
print(score.dtype)  # int32

# 创建数据的时候指定类型
score_2 = np.array([
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
], dtype=np.int64)
print(score_2.dtype)# int 64