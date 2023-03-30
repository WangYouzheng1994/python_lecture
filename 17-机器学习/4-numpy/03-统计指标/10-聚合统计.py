# 聚合统计
import numpy as np

uniform = np.random.uniform(1, 100, (4, 5))
print(uniform)

# max -- start
# 按照行统计每行的最大值~
print(f"行最大值：{uniform.max(axis=1)}")
# 按照列统计每列的最大值
print(f'列最大值：{uniform.max(axis=0)}')
# max -- end

# min -- start
# 按照行统计每行的最小值~
print(f'行的最小值：{uniform.min(axis=1)}')
# 按照列统计每列的最小值
print(f'列的最小值：{uniform.min(axis=0)}')
# min -- end

# mean平均值 -- start
uniform1 = np.array([[1, 2, 3], [1, 2, 3]])
# 按照行统计每行的平均值~
print(f'行的平均值：{uniform1.mean(axis=1)}')
# 按照列统计每列的平均值
print(f'列的平均值：{uniform1.mean(axis=0)}')
# mean平均值 -- end

# 标准差
# 按照行统计每行的标准差值~
print(f'行的标准差值：{uniform1.std(axis=1)}')
# 按照列统计每列的标准差值
print(f'列的标准差值：{uniform1.std(axis=0)}')
# 方差
# 按照行统计每行的方差值~
print(f'行的方差差值：{uniform1.var(axis=1)}')
# 按照列统计每列的方差值
print(f'列的方差值：{uniform1.var(axis=0)}')

# 获取下标 -- start
print(f"行最大值下标：{uniform.argmax(axis=1)}")
print(f"列最大值下标：{uniform.argmax(axis=0)}")
# 获取下标 -- end