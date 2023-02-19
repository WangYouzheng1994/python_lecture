'''
请根据输入的值判断输出 得分等级
    提示语“请输入得分，我会进行判定~”
    < 60不及格
    61~79 达标
    80 ~ 89 良好
    > 90 优秀
'''
score = int(input("請輸入得分，我會進行判定"))
if score < 60:
    print('不及格')
elif 61 <= score <= 79:
    print('达标')
elif score >= 80 and score <= 89:
    print('良好')
elif score >= 90:
    print('优秀')

'''
扩展：
    区间比较
    score > 61 and score < 79
    61 < score < 79:
'''

#    score != None  score is not None
