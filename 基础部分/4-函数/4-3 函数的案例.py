'''
    体温测试
    如果大于37 回复发烧了
    否则是正常
'''
def check_and_print(temp):
    if temp <= 37:
        print("你的体温正常")
    else:
        print("你发烧了，快去看医生")


check_and_print(36.5)


def check_return(temp):
    if temp <= 37:
        return "你的体温正常了"
    else:
        return "你的体温不正常了"


print(check_return(36.5))