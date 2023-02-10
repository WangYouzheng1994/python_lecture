# 占位拼接

name = '小王'
score = 99
print(name + "学python，考了 %s 分，很棒~" )
print(name + "学python，考了 %s 分，很棒~" % score)
text = '实名制夸奖一下'
print(name + "学python，考了 %s 分，%s，很棒~" %(score, text))

'''
    %s 字符串  %d 整数 %f 浮点型
'''
# v_f = 3.55
# print(name + "学python，考了 %s 分，%s，很棒~ 学年成绩 %f" %(score, text, v_f))