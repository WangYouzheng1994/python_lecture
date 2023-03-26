# 生成同坐标系中有多条折线图的案例 subplots
import random

from matplotlib import pyplot as plt

# 解决中文报错问题。
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = 'False' # 这一行干啥用的不知道，先加上

# 假设x轴是天维度
x = range(30)
### 列表生成式：循环30次：相当用根据x轴个数生成每个x轴对应的y点。每次生成的Y值 为 10~15之间左闭右开
# 第一个对象
y = [random.uniform(10, 15) for i in x]
# 第二个对象
y2 = [random.uniform(5, 20) for i in x]

# 自定义x，y刻度
x_label = ["第{}天".format(i) for i in x]
y_label = range(40)  # 现在y的生成式基于 10 ~ 15的

# 创建画布：经过测试没有这个也好使，猜测应该是有默认值....
# plt.figure(figsize=(20, 8), dpi=100)
# 构建一行三个坐标系
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(20, 8), dpi=100)

# 坐标内容中的图形绘制
# plt.plot(x, y, label='张三', color='r', linestyle='--')
# plt.plot(x, y2, label='李四123')
# 第一个坐标系填充数据
axes[0].plot(x, y, label='张三', color='r', linestyle='--')
# 第二个坐标系填充数据
axes[1].plot(x, y2, label='李四123')

# 设置各个坐标系的坐标轴刻度参数
axes[0].set_xticks(x[::3])
axes[0].set_yticks(y[::5])
axes[0].set_xticklabels(x_label[::3])
axes[1].set_xticks(x[::5])
axes[1].set_yticks(y2[::5])
axes[1].set_xticklabels(x_label[::5])

# 设置坐标系的坐标轴其他参数
axes[0].set_xlabel('日期')
axes[0].set_ylabel('数值')
axes[0].set_title('张三', fontsize=35)

axes[1].set_xlabel('日期')
axes[1].set_ylabel('数值')
axes[1].set_title('李四', fontsize=50)

# 设置坐标系的网格效果
axes[0].grid(True, linestyle='--', alpha=0.9)
axes[1].grid(True, linestyle='-', alpha=0.7)

# 设置图例
axes[0].legend(loc=0)
axes[1].legend(loc='best')
# 预览
plt.show()
