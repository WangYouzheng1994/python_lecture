# 定义元祖 tuple
set_1 = (1, 'hello', True)
set_2 = ()
set_3 = tuple()

print(f'set_1元祖的内容为：{set_1}, 类型为：{type(set_1)}')
print(f'set_2元祖的内容为：{set_2}, 类型为：{type(set_2)}')
print(f'set_3元祖的内容为：{set_3}, 类型为：{type(set_3)}')

set_4 = ('hello')  # 这种不是元祖
print(f'set4元祖的内容为：{set_4}, 类型为：{type(set_4)}')

# 注意这个逗号~~
set_4_true = ('hello',)
print(f'set_1_true元祖的内容为：{set_4_true}, 类型为：{type(set_4_true)}')

# 嵌套元祖
set_5_embedding = ((3, 2, 11), (7, 8, 9))
print(f'set_5_embedding元祖的内容为：{set_5_embedding}, 类型为：{type(set_5_embedding)}')

# 下标取值
print(set_5_embedding[1][0])

# 元祖的操作方法
# 返回对应元素的下标
print(set_1.index("hello"))
# 统计某个元素出现的次数
set_6 = (1, 2, 3, 3, 2, 1, 11, 5)
print(set_6.count(1))

# 元祖长度
print(len(set_6))

# while循环迭代


# for 循环迭代
