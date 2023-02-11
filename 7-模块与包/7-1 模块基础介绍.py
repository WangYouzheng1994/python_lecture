'''
[from 模块] import 变量名|函数名字|函数|类 | *  [as 别名]
方括号中的部分可以不写

模块就是一个工具包，每个py文件就是一个模块
在这个模块我们可以定义函数、变量、类（还没学）

模块的抽象作用是：按照功能划分

from import语句 需要写在文件的开头部分！
'''

# Python的time模块是转换日期格式是一个常见的功能。
# 1. import time
# import time
# current_timestamp = time.time()
# print( "当前时间戳为:", current_timestamp)
# 总结这种方式 是需要用 time. 进行调用的

# 2. 直接引入其中的功能
# 引用某个
# from time import time
# # 可以直接调用函数名字了
# print(time())

####
# 引用一部分
# from time import time, localtime, strftime
#
# time_local = localtime(time())
# print(time_local) # 是一种日期对象，封装了日期的完整信息
# # 转换成新的时间格式(2016-05-05 20:28:54)
# time_str = strftime("%Y-%m-%d %H:%M:%S", time_local)
# print(time_str)

####
from time import *
# 直接调用所有函数

# 2. 起个别名
print('模块语法的别名')
import time as time1

print(time1.time())

print('from 语法的部分函数别名')
from time import time as current_time, localtime, strftime as convertTime

time_local = localtime(current_time())
print(time_local) # 是一种日期对象，封装了日期的完整信息
# 转换成新的时间格式(2016-05-05 20:28:54)
time_str = convertTime("%Y-%m-%d %H:%M:%S", time_local)
print(time_str)
