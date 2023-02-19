'''
if 表达式 需要返回boolean:
    # 注意缩进
    逻辑处理
else:

注意： 代码块是通过 4个空格来区分的
'''

'''
逻辑运算符
'''
age = 14

# if age < 6 and age > 0: print('age小于6')
if age < 6 and age > 0:
    print('age小于6')
elif age > 6 and age < 15:
    print('age 在6到15之间')
elif age > 6 and age < 15:
    print('age 在6到15之间')
else:
    print('啥呀？')

# elif 的排他性对比
if age < 6 and age > 0:
    print('age小于6')
elif age > 6 and age < 15:
    print('age 在6到15之间')
if age > 6 and age < 15:
    print('age 在6到15之间')
# 没有elseif 的情况
if age < 6:
    print('age小于6')
else:
    print('age 在6到15之间')

'''
    逻辑运算: and or not
'''
# print(True and False)
# print(True or False)
# print(not (True and False))

'''
    if not 语句为取反的意思
'''
age = 5
if not age > 6: # age 小於等於6
    print('age 小于 等于6')