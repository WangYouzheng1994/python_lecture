"""
学过java的都知道 异常是一层一层向上走的。
python也有相同的异常链的传递 效果类似。

下面通过函数的嵌套调用来模拟异常的向上传递链

即如果当前的函数（方法）报出了异常她会将异常返回到调用他的那个位置，如果调用它的没有处理这个异常 会继续向上抛。
"""


# 定义一个出现异常的方法
def excet1():
    print('---> excet1')
    1 / 0


# 定义一个无异常的方法
def excet2():
    print('---> excet2')
    excet1()


#
def main():
    print('main')
    try:
        excet2()
    except:
        print("搞出来个异常。。。")


if __name__ == '__main__':
    main()

    """
    Traceback (most recent call last):
      File "D:\python实训\10-except异常\2. 异常链.py", line 26, in <module>
        main()
      File "D:\python实训\10-except异常\2. 异常链.py", line 23, in main
        excet2()
      File "D:\python实训\10-except异常\2. 异常链.py", line 18, in excet2
        excet1()
      File "D:\python实训\10-except异常\2. 异常链.py", line 13, in excet1
        1 / 0
        ~~^~~
    ZeroDivisionError: division by zero
    
    
    """
