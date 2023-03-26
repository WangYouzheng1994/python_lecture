# 生成同坐标系中有多条折线图的案例
import random

from matplotlib import pyplot as plt

# 假设x轴是天维度
x = range(30)
# print(type(x))
### 列表生成式：循环30次：相当用根据x轴个数生成每个x轴对应的y点。每次生成的Y值 为 10~15之间左闭右开
# 第一个对象
y = [random.uniform(10, 15) for i in x]
# 第二个对象
y2 = [random.uniform(5, 20) for i in x]
# print(type(y))
# print(y)

# 自定义x，y刻度
x_label = ["第{}天".format(i) for i in x]
y_label = range(40) # 现在y的生成式基于 10 ~ 15的

# 创建画布：经过测试没有这个也好使，应该是有默认值
plt.figure(figsize=(20, 8), dpi=100)
# 坐标内容中的图形绘制
plt.plot(x, y, label='张三', color='r', linestyle='--')
plt.plot(x, y2, label='李四123')

# -- Axis设定 --START
# 设置x轴配置
# plt.xticks(x) # 会显示出从0 ~ 29 很丑
# plt.xticks(x[::5]) # 从0 步进5进行分割，还不错，但是展示不了中文的，因为我们plt.plot中的x就是数字不是中文哈
plt.xticks(x[::5], x_label[::5])  # 配置映射

# 解决中文报错问题。
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = 'False' # 这一行干啥用的不知道，先加上

# 添加坐标轴描述
plt.xlabel("我是x轴")
plt.ylabel("我是y轴")

# 设置y轴配置
# plt.yticks(y_label) 太难看了
plt.yticks(y_label[::5]) # 根据步进分割更符合常理
# -- Axis设定 -- END

# 添加坐标系描述
plt.title("我们的第一个多条数据的matplotlib", fontsize = 40)

# 添加网格：通过注释可以得知 linestyle横线类型 alpha 线的透明度，都是 matplotlib.Line2D中的参数
plt.grid(True, linestyle="--", alpha=0.9)

# 添加图例:https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend，具体loc请参阅文档
plt.legend(loc='best') # 默认自己选
plt.legend(loc=0) # 等价于best 默认自己选
plt.legend(loc=2)

# 预览
plt.show()