# 字面量使用 + 拼接
print('学python，' + "做分析") # 这里的单双引号分开用 没有特殊含义，只是为了复习

# 字符串字面量和字符串变量拼接
name = '小王'
print(name + "学python")

score = 99 # int类型
# score = str(99) # int类型转成str类型就可以拼接了

# python不会触发隐式转换，比较弱, 也就是加号只能是 字符串之间进行拼接
print(name + "学python，考了" + score + "分")


