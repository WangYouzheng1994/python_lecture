"""
成员变量的搜索为 就近原则， 父类继承的成员变量遵循以左为准

对于成员方法，是可以复写的，简单理解就是子类和父类存在相同的成员方法，子类也是可以覆盖父类的，称之为复写。

调用父类成员变量/方法的方法1：
    使用super(). 的方式去调用父类的成员变量和成员方法
调用父类成员变量/方法的方法2：
    使用父类名字.方法名(self)的方式 调用父类成员方法
    使用父类名字.属性名的方式 调用父类成员方法
"""

class Animal:
    name = "动物"

    def who_am_i(self):
        print(self.name)

class Cat(Animal):
    name = "猫"

    def who_am_i(self):
        print(f"我的名字是：{self.name}")
        print(f"我父类的名字是：{super().name}")
        print("调用父类方法StART")
        # 注意！ 这个时候父类方法输出的还是 猫，为什么？ 因为，当前的self 指向的对象是 cat = Cat()
        # 也就是说 是 c调用的 who_am_i，那么这个时候 父类的 who am i中的 self.name 其实是子类的 name
        Animal.who_am_i(self)
        print("调用父类方法EnD")

        print(Animal.name)

cat\
    = Cat()

cat.who_am_i()