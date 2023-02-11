'''
    函数：是组织好的，可以重复使用的 实现特定的功能的代码块 （封装）
    使用函数的好处：随时可以复用的代码，提高开发效率，用以屏蔽功能细节，只关注结果
    python 提供了大量的内置函数
    print(), int(), str(), float(), input(), type()
'''

# len() 判断长度
a = 'asdf'
print(f'字符串长度为 {len(a)}')

# 模拟自定义实现len函数
count = 0
for str in a:
    count += 1

print(count)

'''
def 声明一个函数

'''
def my_len(data):
    count = 0
    for str in data:
        count += 1
    print(f'自定义函数my_len 统计结果：{count}')

'''
使用自定义函数 my_len
'''
my_len('abc')


