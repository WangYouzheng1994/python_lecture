a = "我是python 字符串类型 双引号定义"
b = '我是python 字符串类型 单引号定义'
c = '''我是python 字符串类型 
三引号定义'''
print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))


# 引号的嵌套
print("引号的嵌套---START")
'''
    通过单双引号的错开可以实现 对于引号的输出
'''
a = '"你好"'
print("我是用单引号修饰嵌套的输出：", a)
a = "'你好'"
print("我是用双引号修饰嵌套的输出：", a)
print("引号的嵌套---END")

# a = ""你好"" 这样就不对劲了~ 压根就不认识~

'''
    通过转义字符\实现 单个引号的输出
'''
b = "\"你好\\"
print(b)

b = '\'aaaa'

# \n
a = '1\n2\n3'
print("a : ", a)