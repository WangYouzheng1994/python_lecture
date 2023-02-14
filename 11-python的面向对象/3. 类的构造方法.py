"""
创建对象的时候，希望给这个对象传递参数，传递的方式就是要通过构造方法。

构造方法的特点：1.自动执行，2.如果传递了参数 那么参数也会给到构造方法

"""


class A:
    name = None
    age = 12
    gender = ''

    def __init__(self, name, age, gender):
        """
        定义一个构造函数，接受三个参数 name，age，gender
        :param name:
        :param age:
        :param gender:
        """
        self.name = '小王'
        self.age = age
        self.gender = gender

    def getGender(self):
        """
        注意，成员方法的命名往往以驼峰进行命名
        :return:
        """
        return self.gender

    def getAge(self):
        return self.age

    def getGenderAndAge(self):
        return self.gender, self.age


a = A('a', 0, '女')
print(a.getGender(), a.getAge())

a.age = 22
print(a.getGender())

# 多参数返回一个元祖容器
print(a.getGenderAndAge())