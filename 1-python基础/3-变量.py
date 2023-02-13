"""
    1. 变量是什么，有什么作用
    程序运行中，记录数据用的。
    2. 变量的定义格式
    变量名 = 变量值
    3. 变量的特征
    变量值可以改变
"""

# 单行注释
bianliang = '123'
print(bianliang)
# 字符串 变量
string_a = '123'
string_b = "你好啊"
print(string_a, string_b)
#
# # 数值型-整型
number_a = 666
# # 数值型-浮点型
v_float = 123.12
print(v_float)
#
# # print连续输出
print(123, 456, "123", "我是字符串")

# 多变量同时赋值
bianliang1, bianliang2, bianliang3 = [123,2,3]
print(f"bianliang1={bianliang1}, bianliang2={bianliang2}, bianliang3={bianliang3}")

# 多重复值的深入理解~
"""
赋值的过程是  先计算右边 然后把值给左边的变量。
当出现多重赋值的时候 下面的例子等价于：
a, b = 2, 1
也就是先把 a+b,a 给计算好了然后再给左边的a和b
"""
a = 1
b = 1
a, b = a + b, a
print(a, b)

# 连续赋值
bianliang1 = bianliang2 = bianliang3 = 123
print(f"bianliang1={bianliang1}, bianliang2={bianliang2}, bianliang3={bianliang3}")
