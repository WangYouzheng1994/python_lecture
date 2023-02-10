# 字典的数据结构为 键值对 key/value一对，类似于词典
'''
语法：{key:value, key:value}

特点：
key不可以重复
不可以通过下标获取数据/不能while
可以容纳批量的不同的数据
支持for循环
'''

# 字面量
{'1': '张三', '2':'李四'}

# 变量
my_dict = {'1': '张三', '2':'李四'}
print(my_dict)

# 空
{}
my_dict_emp = dict()
print(my_dict_emp)

# 重复key
my_dict = {'1': '张三', '2':'李四', '1': '王五'}
print(my_dict) # 只有一个

# 根据key获取value
print(my_dict['1'])
print(my_dict)