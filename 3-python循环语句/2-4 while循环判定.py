'''
只要条件满足 就会无限循环
'''
i = 0
while i < 100:  # 这里也是 boolean 判定，只要是true就会一直循环执行
    print(f'目前执行到了, {i}')
    i += 1  # i = i + 1
else:
    print('我结束了哈')  # 当while 条件不满足的时候执行这里

while i < 1:
    print('我小于1')
else:
    print('我一开始就出去了~')

'''
 从1 加到 100 1+2+3+...100的和  目标5050
 提示：一个迭代变量，一个累计加和的变量
'''
idx = 1
sum = 0

while idx <= 100:
    # if idx % 2 == 0:
    # sum += idx
    sum += idx
    idx += 1
else:
    print(f'一到100的和是：{sum}')
