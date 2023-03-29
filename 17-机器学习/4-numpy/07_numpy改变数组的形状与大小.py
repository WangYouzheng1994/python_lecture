import numpy as np
# 生成一个 均值为0，标准差是1的正态分布的4*5的数组
array = np.random.normal(5, 1, (4, 5))
print(f"source_array:{array}")

# 修改形状并生成新数组--START
# 重新修改数组的形状得到一个新数组，注意元素个数必须对应，否则会报错
print(f'reshape to 10*2: {array.reshape([10, 2])}')
# 我不知道有几行，但是我知道有几列，那么行就可以写到-1. 前提还是要求能被整除
print(f'reshape to -1*4: {array.reshape([-1, 4])}')
# 固定行，列让他自己分
print(f'reshape to 5*-1: {array.reshape([5, -1])}')
# 修改形状--END


# 修改原数组大小
array = np.random.normal(5, 1, (4, 5))
print(f'source_array2: {array}')
print(array.resize((5, 4)))
print(array)

# 数组的行列互换 如果是一个4*5的数组 那么就变成5*4
print(array.T)