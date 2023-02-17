class Record:
    name: str = None
    age: int = None
    height: float = None
    weight: float = None
    phone: int = None

    # 使用=none的方式 直接把重载的问题解决了。。有点东西。。 这个地方比java爽太多了
    def __init__(self, name=None, age=None, height=None, weight=None, phone=None):
        """
        定义一个构造函数，接受三个参数 __voltage
        :param __voltage:

        """
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.phone = phone

    def __str__(self):
       return f"name:{self.name}, age:{self.age}, height:{self.height}, weight:{self.weight}, phone:{self.phone}"
