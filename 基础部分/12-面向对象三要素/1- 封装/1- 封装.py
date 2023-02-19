"""
私有的成员内容
"""
class Phone:
    # 私有的成员变量
    __voltage: int = None

    def __get_voltage(self):
        """
        私有的成员方法 __get_voltage
        :return:
        """
        print()
    def getVoltage(self):
        return self.__voltage

    def setVoltage(self, param):
        self.__voltage = param

    def __init__(self, __voltage):
        """
        定义一个构造函数，接受三个参数 __voltage
        :param __voltage:

        """
        self.__voltage = __voltage
        # self.age = age
        # self.gender = gender


p = Phone(1234)
print(p.getVoltage())
p.setVoltage(123)
print(p.getVoltage())
