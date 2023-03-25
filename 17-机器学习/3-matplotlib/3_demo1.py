# 生成折线图案例
import random

from matplotlib import pyplot as plt

x = range(30)
print(type(x))
### 列表生成式：循环30次，每次生成的列表元素值 为 10~15之间左闭右开
y = [random.uniform(10, 15) for i in x]
print(type(y))
print(y)

# 自定义x，y刻度
x_label = ["11点{}分".format(i) for i in x]
y_label = range(40) # 现在y的生成式基于 10 ~ 15的

# 创建画布
plt.figure(figsize=(20, 8), dpi=100)
# 图形绘制
plt.plot(x, y)
# 设置x轴
# plt.xticks(x) # 会显示出从0 ~ 29 很丑
# plt.xticks(x[::5]) # 从0 步进5进行分割，还不错，但是展示不了中文的，因为我们plt.plot中的x就是数字不是中文哈
plt.xticks(x[::5], x_label[::5]) # 配置映射

# 解决中文报错问题。
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = 'False' # 这一行干啥用的不知道，先加上

# 添加网格：通过注释可以得知 linestyle横线类型 alpha 线的透明度，都是 matplotlib.Line2D中的参数
plt.grid(True, linestyle="--", alpha=0.9)

# 添加坐标轴描述
plt.xlabel("我是x轴")
plt.ylabel("我是y轴")

# 添加坐标系描述
plt.title("我们的第一个matplotlib", fontsize = 40)

# 设置y轴
# plt.yticks(y_label) 太难看了
plt.yticks(y_label[::5]) # 根据步进分割更符合常理
plt.show()


# ----------------
