# 数据转换
# 显式转换、

'''
1. 将x转换成整数，并返回
int(x)
2. 将x转换成浮点数，并返回
float(x)
3. 将x转换成字符串，并返回
str(x)
'''
print(type(int('123')))
# 反例
# print(int('sadf123'))


# 浮点转整数会丢失精度，并没有进行四舍五入
print(int(123.9321))
#
# # 隐式转换
#
# print("变量的转换")
print("####演示示例 START")
var_str = '3333'
var_num= 123
var_float = 123.444444
#
print(int(var_str))
print(float(var_num))
print(str(var_float))

print("####演示示例 END")

#
print(type(int(var_str)))
print(type(float(var_num)))
print(type(str(var_float)))