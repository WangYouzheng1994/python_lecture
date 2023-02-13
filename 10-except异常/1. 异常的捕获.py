"""
语法：
try:
    代码块1
except:
    异常出现后的代码块
else:
    如果代码块1中没有出现异常的话的在代码块1执行完以后 执行这里
finally:


"""


def all_except():
    try:
        with open('f:\\123.tdx', 'r') as file:
            pass
    except:
        print('指定是有点毛病~')

    # 捕获全部异常的常见写法
    try:
        print(1 / 0)
        print(aaa)
    except Exception as e:
        print(e)


"""
捕获指定类型的异常

异常是有类型的
FileNotFoundError: No such file or directory
NameError: xxx is not defined
IndexError: index out of range
ZeroDivisionError: division by zero 1 / 0
"""


def exacly_multi_except():
    try:
        print(1 / 0)
        print(aaa)
    except NameError as e:
        print(e)
    except ZeroDivisionError as b:
        print(f'你是不是把0当除数啦！~ {b}')


def any_except():
    """
    平行捕获多个异常，这相当于定义了一个元祖
    :return:
    """
    try:
        print(aaa)
        print(1 / 0)
    except (ZeroDivisionError, NameError) as b:
        print(f'你是把我当除数了还是没声明： {b}')


def no_exception_else():
    """
    没有异常运行else
    :return:
    """

    try:
        print("asdf")
        return 123  # return语句存在的时候 else不执行哈~
    except:
        print('我有异常')
    else:
        print("我是else")


def exception_finally():
    """
    异常 finally
    :return:
    """
    try:
        print("asdf", 123)
        1 / 0
    except:
        print("异常啦")
    else:
        print("else，没有异常的执行else")
    finally:
        print("finally-无论是否异常都会运行")


# exacly_multi_except()
# any_except()
# no_exception_else()
exception_finally()