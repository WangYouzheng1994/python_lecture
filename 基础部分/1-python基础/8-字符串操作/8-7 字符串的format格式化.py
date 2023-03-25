
# 字符串使用format格式化，注意：1. 转义字符针对于特殊的{} 左右括号无效。 如果需要使{、} 那么就用{{、}}
variable_name = '小王'
birth_day = '2000-01-01'
salary = 1200.50
print("我是{}, 我出生于{}, 我的薪水\"是{{salary}}".format(variable_name + str(salary), birth_day, salary))

