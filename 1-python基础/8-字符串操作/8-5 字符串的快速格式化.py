'''
    高级语言都会有这种方式
    1. 不限制数据类型
    2. 不控制数据精度
    3. 就是把所有数据转成字面量进行拼接 （背后触发了隐式转换）
'''
variable_name = '小王'
birth_day = '2000-01-01'
salary = 1200.50

# 语法 f""，在字符串中 {变量名称}
print(f"我是{variable_name}, 我出生于{birth_day}, 我的薪水是{salary}")

print(salary)
print(str(salary)) #不是print去掉了0