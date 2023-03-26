import matplotlib.pyplot as plt

# 展示分类的统计能力

# 解决中文报错问题。
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = 'False' # 这一行干啥用的不知道，先加上


x = ['青岛', '北京', '上海']

y = [1500, 3000, 3100]

plt.figure(figsize=(20, 8), dpi=100)
plt.bar(x, y, width=0.3, color=["b", 'g', 'r'])

plt.xlabel("城市名称")
plt.ylabel('工资情况')

plt.title("青岛北京上海的工资对比情况", fontsize=50)
plt.grid(linestyle='--', alpha=0.9)

plt.show()