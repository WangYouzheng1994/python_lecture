'''
    python中的None  对应了 数据库中的null的概念
    因此当函数没有返回值的时候 这个函数其实返回的是None

'''

a = None
print(type(a))
# 接受没有返回值的函数

def none_func():
    a = 0
    a = a + 1
    a += 1

print(type(none_func()))

#主动返回None

def return_none():
    return None


print(return_none())
print(type(return_none()))

'''
    扩展：了解
    None值的判定为false
    数字0 为false 非0 为true
'''
a = -1
if a:
    print(a)
else: print('none')