'''
    变量的作用域 有两种：局部和全局
'''
# 全局
a = 1

# x为局部变量
def func(x):
    print(a)
    print(x)
func(22)

# 会报错
#print(x)


# 在函数内部定义全局变量 (有空就了解一下~) 关键字：global
def func(x):
    global xx
    xx = x
    print(a)
    print(xx)
func(22)
print(xx)

# 引出变量的“就近原则”
def func_3(a) :
    print(a)
func_3(5)
print(a)

'''
    精讲堆栈内存理念 便于引出后续的 数据集合概念与对象的概念
'''