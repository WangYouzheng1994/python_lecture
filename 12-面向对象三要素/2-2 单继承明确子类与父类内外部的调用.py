"""
多继承情况下，子类继承父类的成员变量的优先级是根据继承列表由左到右侧顺序来的
"""


class GrandParent:
    a = 0


class Parent(GrandParent):
    # a = 1
    aa = 1
    def p_func(self):
        print(self.aa)


class Parent_2:
    a = 12
    p2_a = 'p2_a'

    def def_func(self):
        print(self.p2_a)


class Child(Parent, Parent_2):
    # a = 2

    def c_func(self):
        # print(f"self.a的值是:{self.a}, parent.a{super.a}")
        print(f"self.a的值是:{self.a}")


c = Child()
c.c_func()
c.def_func()
# 多继承情况下先找自身的a，如果自身没有。会按照继承列表中由左到右的方式寻找
print(c.a)