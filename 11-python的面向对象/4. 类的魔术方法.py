"""
1. 字符串方法 __str__ 如果不重写，默认的print就是内存地址。
"""


class B:
    aa: 1
    bB: 2

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

    def __str__(self):
        # 重写了str以后 print打出来的就不是内存地址了
        return f'当前对象的name是{self.name}, age是{self.age}'


b = B('张三', 18, '女')
print(b)

"""
对象类型如果不定义 那么我们定义的这个类的实例是不能比较的，会报异常，原因是复杂类型是有自己多维度属性的，具体的比较方式需要人工设定。

2. 小于符号的比较 __lt__ 
如果定义了 __lt__ 那么，可以实现 < 的运算。 低版本python可以实现 < 和 > 的运算
3. 小于等于符号的比较 __le__ 
4. __gt__
5. __ge__
6. __eq__
"""


class Diff:
    number = None

    def __lt__(self, param):
        """
        :param 被比较的变量
        :return: 布尔
        """
        # 实现多元化的比较方式：1. 对象-数值。 2. 对象-对象
        if param is not None:
            return False


        if (type(param) == Diff):
            return self.number < param.number
        else:
            return self.number < param

    def __gt__(self, param):
        """
        大于比较的运算
        :param 被比较的变量
        :return: 布尔
        """
        return self.number > param

    def __le__(self, param):
        """
        大于比较的运算
        :param param:
        :return:
        """
        return self.number <= param

    def __ge__(self, param):
        """
        大于等于的比较运算
        :param param:
        :return:
        """
        return self.number >= param


d = Diff()
d.number = 10
print(f'd < 15的运算, {d < 15}')
print(f'd <= 15 小于等于的运算：{d <= 15}')
print(f'd > 15 大于的运算：{d > 15}')
print(f'd >= 15 大于等于的运算：{d >= 15}')

# 数据类型的缩写为
"""
int 
float
string
list
tuble
set
map
boolean
"""
print(f'基本数据类型 start')
print(type(12) == int)
print(type(1.1) == float)
print(type('123') == str)
print(type([1, 2, 3]) == list)
print(type((1, 2, 3)) == tuple)
print(type({1, 2, 3}) == set)
print(type({'1': 1}) == dict)
print(type(False) == bool)
print(f"基本数据类型 end")

"""
引用类型实例的判定
"""
print(type(d) == Diff)

