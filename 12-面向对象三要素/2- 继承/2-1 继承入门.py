"""
单继承语法
class Parent:
    a = 1

class Child(Parent):
    a = 2

"""

class Parent:
    # a = 1
    aa = 1
    def p_func(self):
        print(self.aa)


class Child(Parent):
    a = 2


p = Parent()
c = Child()
print(p.aa)
print(c.a)
# 从父类继承下来的
print(c.aa)
c.p_func()



