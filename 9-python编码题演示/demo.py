# 4. 下面程序的执行结果
sum = 0  # 注意 这个其实没用 他是全局变量
for item in range(1, 100):
    sum += item  # 这里才是局部变量
    if item == 5:
        print(sum)
        break
else:
    print(-1)


# 10.	下面的代码是否能够正确运行，若不能请解释原因；
# 迭代过程中操作 del 删除元素是不合法的，会出现下标越界的异常
# x = list(range(20))
# for i in range(len(x)):
#     del x[i]


# 加时间例子
def plus_time():
    """
    接收一个时分秒，然后给他增加五小时零30秒
    :return:
    """
    hour, minute, second = input('请输入时间(h:m:s): ').split(":")
    hour = int(hour)
    minute = int(minute)
    second = int(second)

    # 秒数
    plus_second = 30 + 5 * 60 * 60

    # 将当前的时分秒也转换成秒数
    input_time_second = hour * 60 * 60 + minute * 60 + second

    # 将叠加后的秒数再转成时分秒
    new_time_second = input_time_second + plus_second
    # 小时 = 秒数 / (60 * 60)
    # 分钟 = 用 小时 取余后的值 / 60，即： 秒数 % (60 * 60) / 60
    # 秒数 = 要么用所有秒数直接取余60， 或者用分钟计算后的余数 然后去除60。
    new_hour = int(new_time_second / (60 * 60))
    new_minute = new_time_second % (60 * 60) // 60
    new_second1 = new_time_second % (60 * 60) % 60
    new_second = int(new_time_second % 60)
    # print("除法会有小数返回值因此如果不用//符号 那么就得 加上int()")
    # print(type(5 // 2))
    # print(type(5 % 2))
    print(f'结果是：{new_hour} : {new_minute} : {new_second}')
    print(f'结果是：{new_hour} : {new_minute} : {new_second1} / {new_second}')


# plus_time()


# 斐波那契例子：这个例子实现了斐波那契的指定遍历次数后的结果展示，先做了解
def fibonacci_sequence(stop_index):
    """
    斐波那契数列的结果示例：
    1、1、2、3、5、8、13、21、34
    解释：
    第一个值+第二个值等于第三个值
    第四个值等于 第二个+第三个值

    总结为：当前值加上前两个值作为自己的值
    :return:
    """
    a1 = 0
    a2 = 0
    # a3 = 0 # current值
    idx = 0  # 迭代的个数
    while idx < stop_index:
        # print(a3) 报错
        # 都是0 证明是第一轮
        if a1 == 0 and a2 == 0:
            a3 = 1  # 注意这里的作用域 如果外层没有定义current 依然好用。 也就是说只要在函数内部任意嵌套层级声明 其以下位置代码都可用~
        else:
            a3 = a1 + a2
        print(a3)  # 这轮的值打印出来了
        # 把这轮的a1 变成a2 原因是 下轮的a1 需要是这轮的第二个值
        a1 = a2
        # 下轮的a2 需要是这轮的当前值
        a2 = a3
        idx += 1


# fibonacci_sequence(5)  # 第一个到第五个斐波那契的打印输出

# 斐波那契数列为1,2,3,5,8,13,21.....根据这样的规律，编程求出400万以内最大的斐波那契数，并求出他是第几个斐波那契数。
def fibonacci_sequence2(n):
    """
    # 这个题干的要求是，算出来一个指定数值上限内的最大斐波那契数
    以下代码基于python官方demo 进行改写处理，注意其中的多重赋值逻辑
    :return:
    """
    # 第一个值
    a = 0
    # 第二个值
    b = 1
    # 计数
    m = 0
    # 上述代码可以改成 a,b,m = 0,1,0
    while b <= n:
        a, b = b, a + b
        m += 1
    else:
        print(f"最大值为：{a}，是{m-1}个位置")

    """
     # 注意这种多重赋值写法
     a, b = 3, 1 
    """
    # a, b = a + b, a  # 这种写法解决的中间变量的值传递
    # print(a, b)

fibonacci_sequence2(13)