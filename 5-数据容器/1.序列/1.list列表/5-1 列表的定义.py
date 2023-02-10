'''
    列表的声明语法：
    字面量[元素1, 元素2, 元素xxx, ... 元素n]
    变量
    变量名字 = 字面量[元素1, 元素2, 元素xxx, ... 元素n]

    元素：列表中的每一份数据都是一个元素，元素的类型没有限制~

    列表的特點： 可以容纳非常的元素
    可以容纳不同类型的元素
    元素是有序存储（保持插入序）
    允许元素内容重复
    列表可以修改
'''

# 字面量: 字符串， 数字， boolean
['123', 123, True]

# 变量
mylist = ['123', 123, True]
print(mylist)
mylist =[]
print(mylist)
print(type(mylist)) # <class 'list'>
emptylist = list()
print(emptylist)
