"""
class 类名
类：认为是现实生活中每种物品或者客观存在的物体的一种抽象的描述。它具备属性与行为。就像人有身高属性，吃饭睡觉的行为一样。

类名的表写格式要求：
1. 首字母大写

面向对象编程称之为OOP
类和对象的关系为：图纸与实物的关系。
"""
# 设计类
class Student:
    name = None
    gender = None

# 创建对象
stu_1 = Student()
stu_2 = Student()

# 为创建的对象的属性进行赋值
stu_1.name = '肖飞'
stu_1.gender = '男'

stu_2.name = '小姜'
stu_2.gender = '女'


