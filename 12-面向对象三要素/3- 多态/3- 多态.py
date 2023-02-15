"""
抽象方法：内部没有任何方法，直接用pass填充的
抽象类是一种顶层设计约束。
"""
class Animal:
    def eat(self):
        pass
    def sleep(self):
        pass


class Cat:
    def eat(self):
        print("cat eat")
    def sleep(self):
        print("cat sleep")


class Dog:
    def eat(self):
        print("dog eat")

    def sleep(self):
        print("dog sleep")


a = Dog()
a.eat()
a.sleep()

c = Cat()
c.eat()
c.sleep()
