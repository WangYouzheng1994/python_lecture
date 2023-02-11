'''
    嵌套for循环，关键点 控制好 “缩进”
'''

i = 1
range_inside = range(1, 5)
for i in range(1, 101):
    print(f"今天是努力的第{i}天")
    for ii in range_inside:
        if ii == 2:
            continue
        if ii == 3:
            break
        print(f"我学了 {ii}个知识点")
    print(f"第{i}天，努力结束~")
    if i == 5:
        break
print("搞定了哈")