import matplotlib.pyplot as plt

# 画布
plt.figure(figsize=(20, 8), dpi=100)
# 图像绘制
x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]
plt.plot(x, y)


# 保存结果 不能先show，否则会是空白的~
plt.savefig('matdemo.jpg')
# 展示 show会释放figure的资源，类似于 show完了就刷新了。
plt.show()