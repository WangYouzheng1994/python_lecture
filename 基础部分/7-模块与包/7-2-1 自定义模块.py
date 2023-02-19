"""
语法相同：
1.引入整个模块（文件） import 模块名
2. 引入某个文件的函数 from 模块名 import 函数名

"""
# import qs_util
#
# print(qs_util.add(1, 2))
# qs_util.my_print(12321312)


# 测试 from qs_util import *
# 1. 当我们没有在qs_util中声明内置变量的值的时候
# from qs_util import *
# my_print('321321312')# 看不到这个方法~ 如果要看到 就需要在已定义的__all__里面加上 my_print
# print(add(1, 2))
from qs_util import my_print
my_print('ffffffffff') # 能看到了~