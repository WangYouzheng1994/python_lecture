'''
if 表达式 需要返回boolean:
    # 注意缩进
    逻辑处理
    if 条件2:
        xxx
    elif xxx:
        xxx
else:
'''

'''
核心是缩进
'''
if int(input('你身高是？')) > 120:
    print('太高了，不免费')
    if str(input('你是会员嗎?')) == '是':
        if int(input('你是几级会员？')) > 3:
            print('三级以上，你可以免费！')
        else:
            print('不好意思，你得买票了哈')
    else:
        print('不好意思，你得买票了哈')
else:
    print('小孩子，随便玩。')
