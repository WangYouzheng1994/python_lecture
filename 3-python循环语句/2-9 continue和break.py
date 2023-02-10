'''
    coninue和break
    用以控制循环语句的终止行为

    continue: 跳过此轮循环 进入下轮循环
    break：结束此次循环行为

    他们的控制范围都是所在的循环内
'''

for item in range(0, 10):
    if item <= 3:
        print(f'item: {item}')
    elif item > 3 and item < 7:
        continue
    else:
        print(item)