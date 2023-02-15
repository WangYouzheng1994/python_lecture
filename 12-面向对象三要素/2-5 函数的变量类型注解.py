"""
函数的参数列表与返回值类型定义
语法与变量注解一样

def 函数名字(变量名字: 类型, 变量名字: 类型.....) -> int:
    pass
"""


def my_func(v_int: int, v_str: str):
    pass


def my_func(v_str: int, v_int: str):
    pass


def plus(param1: int, param2: int) -> int:
    return param1 + param2


print(plus(2, 5))


