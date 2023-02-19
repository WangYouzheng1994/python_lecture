# 函数传递函数：用于计算逻辑的封装传递。lambda表达式的支撑。行为传递

def my_fun1(args):
    print('我在处理我的逻辑')
    args(111)
    print('我可以调用别的函数')
def my_arg_fun(a):
    print(f'我是内部函数了哈{a}')

my_fun1(my_arg_fun)