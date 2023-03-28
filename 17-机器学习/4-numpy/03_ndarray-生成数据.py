import numpy as np
# 生成数组api - 生成0和1元素的数组，传入shape
ones = np.ones([4, 8]) # 4行*8列 的元素值都为1的数组
zeros = np.zeros([2, 2]) # 2行*2列的 元素值都是0的数组

print(ones)
print(type(ones))
print(zeros)
print(type(zeros))

zeros_like = np.zeros_like(ones)
print(zeros_like)

# 生成数组api - 从现有数组生成
# 根据已有数组创建一个新的，深拷贝
array = np.array(ones)
array[1][0] = 5
print(f'array:{array}')
print(f'ones:{ones}')
# 根据已有数组创建一个索引，浅拷贝
asarray_index = np.asarray(array)
asarray_index[0][1] = 123
print(f'asarray_index:{asarray_index}')
# 可以看到把array给修改了
print(f'array:{array}')
array[1][0] = 6
print(f'array:{array}')
print(f'asarray_index:{asarray_index}') # 可以看到asaray_index也改了

# 生成数组api - 生成间隔的数组
# 从数字0 到 100， 进行生成5个数，自己判定间隔
print(np.linspace(0, 100, 5))
# 从数字1 到5  生成两个数
print(np.linspace(1, 5, 2))

# 从数字10 到50 间隔2位进行生成
print(np.arange(10, 50, 2))

# 生成等比数列：以下是构造10的指数，构造三个，指数从0到2：即10的0次幂，10的1次幂，10的2次幂：默认的基数就是10，
#https://blog.csdn.net/zhouhaomy/article/details/121733014
print(f'np.logspace:{np.logspace(0, 2, 3)}')
print(f'np.logspace:{np.logspace(0, 2, 5)}')
print(f'np.logspace2的从1到3次幂:{np.logspace(1, 3, 3, base=2)}')

# 生成随机数组：从0~1之间的 一行三列的数组
print(f'np.random.rand的随机数组:{np.random.rand(1, 3)}')
# 生成随机数组：指定开始和结束的随机采样数组，左闭右开：从5~50选30个数
print(f'np.random.uniform，从5~50选30个数{np.random.uniform(5, 50, 30)}')
# 生成随机数组，样式为3*10
print(f'np.random.uniform(5, 50, (3, 10))：{np.random.uniform(5, 50, (3, 10))}')

# 生成随机数组，元素值是int的，上面的都是float的：生成一个三行五列的数组，采样范围是1~10
print(f'np.random.randint(1, 10, (3, 5)):{np.random.randint(1, 10, (3, 5))}')
# 生成随机数组：元素值是int，生成五个数
print(f'np.random.randint(1, 10, 5): {np.random.randint(1, 10, 5)}')
print(f'np.random.randint(1, 10, (0, 5)): {np.random.randint(1, 10, (1, 5))}')
