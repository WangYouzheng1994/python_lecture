'''
    体温测试
    如果大于37 回复发烧了
    否则是正常
'''
def check(temp):
    if temp <= 37:
        print("你的体温正常")
    else:
        print("你发烧了，快去看医生")

check(36.5)