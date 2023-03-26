import numpy as np

# 创建adarray，定义一个二维数组：两行五列。
score = np.array(
    [
        [1,2,3,4,5],
        [1,2,3,4,5]
    ]
)

print(score)
print(score[0][1]) # 第一行第二列
print(score[0][4]) # 第一行第5列


# --- 比较原生list 会发现numpy的计算效率更高。
import random
import time

# 定义一个序列a
a = []
# 循环一亿次
for i in range(100000000):
    a.append(i)
else :
    print('插完了')

# 原生序列转 nparray
b = np.array(a)

# %time sum1=sum(a) jupyter才能用%time
astart =time.perf_counter()
sum1=sum(a)
aend = time.perf_counter()
print('原生序列耗时:{}'.format(aend - astart))
# %time sum2=np.sum(b) jupyter才能用%time
bstart = time.perf_counter()
sum2=np.sum(b)
bend = time.perf_counter()
print("nparray计算耗时：{}".format(bend- bstart))