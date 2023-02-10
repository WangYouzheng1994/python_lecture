'''
if 表达式 需要返回boolean:
    # 注意缩进
    逻辑处理
else:
'''

age = 14

if age < 6:
    print('age小于6')
elif age > 6 and age < 15:
    print('age 在6到15之间')

if age < 6:
    print('age小于6')
else:
    print('age 在6到15之间')


'''
    if not 语句为取反的意思
'''
age = 5
if not age > 6:
    print('age 小于 等于6')