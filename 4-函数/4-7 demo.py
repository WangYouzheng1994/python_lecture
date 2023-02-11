# # 全局变量
# a = 1
#
# # x为局部变量
# def func(x):
#     a = 2 # 就近原则
#     print(a)
#     print(x)
# func(22)
# print(a)
# # print(x)



a = 123

# 在函数内部定义全局变量 (有空就了解一下~) 关键字：global
def func(x):
    # a = 234 # 如果在global之前定义，他会报错提示重复
    global a
    a = 2
    print(a)
    print(x)
func(22)
print(a)







