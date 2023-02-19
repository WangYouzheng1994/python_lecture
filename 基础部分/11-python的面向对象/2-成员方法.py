class Student:
    # 属性 称之为成员变量
    name = None
    gender = None

    # 行为 成员方法
    def say_my_name(self):
        """
        输出自己的name
        :return:
        """
        print(self.name)

    def eat(self):
        """
        输出自己的吃
        :return:
        """
        print('到点了到点了 得吃饭了！')

    def run(a, self, b):
        """
        test self
        :param self:
        :return:
        """
        print(a)

        print(b)
        print(self)
        print(a.name)


# 创建对象
stu_1 = Student()

# 为创建的对象的属性进行赋值
stu_1.name = '肖飞'
#
# stu_1.say_my_name()
# stu_1.eat()
stu_1.run("a", b=123)

"""
成员方法和普通函数的定义 有区别，核心就是参数列表中的必须要有self且self得定义到第一个位置
self的作用是，如果要访问自身对象中的成员变量/成员方法的时候就需要用此self

经过run()的传入参数测试，其实是成员方法的第一个参数就是self，我们可以给他重命名，而且传参的时候 他是透明的。

以上，总结：
1.self相当于其他编程语言中的this
2.在class的funciton中默认第一个参数就是self
3.在调用成员方法的时候self认为是透明的不存在的。
"""

# 私有变量的使用方式


