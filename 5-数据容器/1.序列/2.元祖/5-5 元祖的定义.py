"""
    元祖tuple与序列list对比的不同点：1.去重，2.一旦定义就不可以修改及封装好的数据就不能够修改了

"""


# 定义元祖 tuple，使用小括号定义，用逗号分割不同的数据，数据允许是不同的类型
# 元祖的字面量
('aa', 123, False)
# 元祖变量
set_1 = (1, 'hello', True)
set_2 = () # 空元祖
set_3 = tuple() # 空元祖 对象方式

print(f'set_1元祖的内容为：{set_1}, 类型为：{type(set_1)}')
print(f'set_2元祖的内容为：{set_2}, 类型为：{type(set_2)}')
print(f'set_3元祖的内容为：{set_3}, 类型为：{type(set_3)}')

set_4 = ('hello')  # 这种不是元祖，是字符串
print(f'set4元祖的内容为：{set_4}, 类型为：{type(set_4)}')

# 注意这个逗号~~
set_4_true = ('你好 我才是真的元祖哈',) # 加上一个逗号 才是字符串
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

# 元祖长度 使用len函数
print(f'我这个元祖的长度是：{len(set_6)}')

