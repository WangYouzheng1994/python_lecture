"""
私有的成员内容
"""
class Phone:
    # 私有的成员变量
    __voltage = None

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

p = Phone()
# p.__get_voltage()
p.setVoltage(123)
print(p.getVoltage())
