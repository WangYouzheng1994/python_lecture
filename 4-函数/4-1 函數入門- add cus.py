# 定义一个有参数的函数 xiaojiang 接受两个参数(x, y 被称之为输入参数)，
# 这个函数 会计算 x + y的值，并返回结果
def xiao_jiang(x, y):
    result = x + y  # 整型和浮点型相加 触发了隐式转换
    return result
# 调用add方法 1 和 2.3 为实参
print(xiao_jiang(1, 2.3))
print(xiao_jiang(2, 2))
print(xiao_jiang(5, 5))