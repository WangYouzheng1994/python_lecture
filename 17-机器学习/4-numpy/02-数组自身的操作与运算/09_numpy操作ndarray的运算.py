# ndarray的运算

import numpy as np

np_array = np.array([1, 2, 3, 4])
# 大于1的结果集，默认返回True/False
print(np_array > 1)

random_arr = np.random.normal(0, 15, (8, 10))
print(random_arr > 1)
print(type(random_arr))

# random_arr里面>1的元素 直接进行替换为值12
random_arr[random_arr > 1] = 12
print(random_arr)

# 通用判断函数
# random_arr都大于0 返回True
print(f'通用判断函数np.all: {np.all(random_arr > 0)}')
# random_arr任意大于1 返回True
print(f'通用判断函数np.any: {np.any(random_arr > 1)}')

# np.where 三元运算符
# 判定每个元素 如果 > 1 ，那么该元素就是1，否则就是0，响应一个新数组
print(np.where(random_arr > 1, 1, "不对劲了"))

# 三元运算符的复合使用np.logical_and() / np.logical_or()
print(np.where(np.logical_and(random_arr >= 1, random_arr == 12), "大于1 并且等于12", "不满足"))
print(np.where(np.logical_or(random_arr <= 12, random_arr == 1), "小于等于12 或者 等于1", "不满足"))
