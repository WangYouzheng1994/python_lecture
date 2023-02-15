"""
类型注解提示，不限制类型
类型注解的目的是便于开发环境IDE做类型推断
为开发人员提供数据类型的说明

语法1:
变量: 类型 = 值
语法2:
注释中 # type: 类型
"""

"""
变量的注释
"""
v_a: str = "123"
v_b: int = 123

"""
容器的类型注释
"""
# 表示 my_list 是list类型
my_list: list = [1, 3, 5]
my_str: str = "1, 3, 5"
my_tuble: tuple = (1, 3, 5)
my_set: set = {1, 3, 5}
my_dict: dict = {"a": 1, "c": 3, "b": 5}

# 可以更进一步 表示容器内部的数据类型
my_list: list[int] = [1, 3, 5]
# my_list: list[int, str, float] = [1, 3, 5] 类型不同不限制
my_list: list[int, str, float] = [1, "3", 5.112]
my_dict: dict[str, float] = {"zhangsan": 5.12, "lisi": 4.15}

"""
注释中进行类型注释
"""
v_a = "123"  # type:int
my_list = [1, 3, 5]  # type: list
my_list = [10, 20, 30]  # type: list[int]