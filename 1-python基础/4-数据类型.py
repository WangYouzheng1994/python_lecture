# type()函数 可以查看字面量与变量“存储”的数据类型
# 方法1： 使用print输出type对应的类型信息
print(type('字符串字面量'))
print(type(666))
print(type(11.3333))

print("----输出字面量类型---END")

 # 方法2： 使用变量存储type()语句的结果
string_type = type("字符串字面量")
int_type = type(666)
float_type = type(13.555)
print(string_type)
print(int_type)
print(float_type)
print('----输出变量存储的type转换后的结果值 END')
#
# 方法3： 使用type()语句，查看变量中存储的数据类型信息
str_variable = '字符串变量'
int_variable = 123
float_variable = 123.555

print(type(str_variable))
print(type(int_variable))
print(type(float_variable))
#
print("----输出变量类型---END")

