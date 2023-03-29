import numpy as np

float_uniform = np.random.uniform(0, 500, (2, 8))
print(f'source_arr:{float_uniform}, dtype:{float_uniform.dtype}')
# 元素全部转换成 int32
target_arr = float_uniform.astype(np.int32)
print(f'astype_target:{target_arr}, dtype:{target_arr.dtype}')

# 转成byte
print(target_arr.tostring())

# 数组的去重
multi_item_arr = np.array([1,2,2,3])
print(multi_item_arr.size)
unique_arr = np.unique(multi_item_arr)
print(unique_arr)
print(type(unique_arr))












