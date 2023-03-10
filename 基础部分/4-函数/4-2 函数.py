'''
    函数的定义结构

    def 函数名(参数列表) :
        函数体
        return 返回值
    1. 参数列表可以省略
    2. 返回值 return 可以省略
    3. 必须先定义后使用，使用方式：函数名字()
    4. 参数列表 长度不限
'''

'''
案例： 编写一个能打印输出任何字符的一个程序，函数名称随便
'''

def print_cus():
    print('我是一个函数哈')

print_cus()

def print_cus_2():
    print(input('请输入您需要我打印的内容~'))

print_cus_2()


# 定义一个有参数的函数 接受两个参数(x, y 被称之为形参)，并返回两个参数的和
def add(x, y):
    result = x + y  # 整型和浮点型相加 触发了隐式转换
    return result
# 调用add方法 1 和 2.3 为实参
print(add(1, 2.3))

