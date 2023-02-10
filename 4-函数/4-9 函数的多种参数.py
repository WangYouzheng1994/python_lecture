
# 关键字传参 关键字参数可以不考虑顺序
def my_fun(a, b, c):
    print(a, b, c)
    return None

# 显示指定对应的形参变量名
my_fun(b = 1, a = 3, c = 2)

# 位置参数与关键字参数混用

# 这个会报错 因为同时给了a
# my_fun('aaaa', a=3, c=2)
# 正确的混用，位置参数在前，关键字参数可以不考虑顺序
my_fun('aaaa', b=3, c=2)

# 默认参数 设置b这个参数默认为2
# def my_fun(a, b=2, c): 默认参数往后放
def my_fun(a, c, b='i am default argument'):
    print(a, b, c)
    return None

my_fun(1,2)


# 不定长参数 可变参数， 其实就是给了一个数据集合类型的参数罢了
# 1. 元祖类型
def my_fun(*args):
    print(args)
    print(type(args))
    return 123
my_fun(1,2,5,11,4)
# 2. 转成dict 字典
def my_fun(**args):
    print(args)
    print(type(args))
    return 123
my_fun(a1='', a2='bb') # 必须是键值对类型