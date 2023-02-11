'''
    使用辅助符号"m.n"来控制数据的宽度和精度
    m 控制宽度，认为是整个数据的长度（小数点和小数部分也要算入宽度的计算），宽度不够会用空格补全
    n 控制小数点精度，会进行四舍五入
'''

# 1. 将整数的宽度控制在5位
a = 123
'%(m.n)d'
print("开始控制成五位~ %5d" % a)

# 2. 宽度控制为5，精度为2
a = 123456.1234
print("宽度控制为5，精度为2~ %5.2f" % a) # 宽度只会补齐，超出不管。
a = 6.1264
print("宽度控制为5，精度为2~ %5.2f" % a) # 精度会进行四舍五入
