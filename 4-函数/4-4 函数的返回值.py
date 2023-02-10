'''
    函数在调用后，给调用者返回结果
'''

# 定义一个有参数的函数 接受两个参数(x, y 被称之为形参)，并返回两个参数的和
def add(x, y):
    result = x + y  # 整型和浮点型相加 触发了隐式转换
    return result
    # return 后面的代码不会执行
    print("我在result后面哈")


print(type(add(1, 55.3)))