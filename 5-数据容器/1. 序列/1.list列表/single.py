# mylist = [['dog', 'cat'], ['青岛', "济南", "潍坊", "烟台"], ['山东省', '陕西省', '湖北省', '四川省']]
#
# # [['dog', 'cat'], ['青岛', '济南', '潍坊', '烟台'], ['山东省', '陕西省', '湖北省', '四川省']]
# # print(mylist)
# # print(type(mylist[0]))
# print(mylist[0])
# # mylist_1 = ['dog', 'cat']
# # print(mylist_1[1])
# print(mylist[0][1])

mylist = ['小狗', '小猫', '小老虎']
# print(mylist)
# # # print(mylist.index('小老虎'))
# # mylist[1] = '小猫~~~'
# #
# # print(mylist)
# # mylist[-2] = '猫'
# # print(mylist)
#
# mylist.insert(1, 123)
# mylist.insert(40, '乌龟')
# print(mylist)
# mylist.append("我是第一个")
# mylist.append("我是第二个")
# print(mylist)
#
# last_list = ["我是追加容器的第一个值", "我是追加容器的第2个值", "我是追加容器的第3个值"]
# mylist.extend(last_list) # 把last_list 追加到list最后
#
# print(mylist)
#
# # 移除的第一种方法
# del mylist[1]
# print(mylist)
#
# pop_var = mylist.pop(4)
# print(mylist)
# print(pop_var)
#
# mylist.remove("乌龟")
# print(mylist)
#
# # mylist.clear()
# mylist.extend(['老鼠', '老鼠1', '老鼠'])
# print(mylist)
# print(mylist.count('老鼠'))
# print(len('你好啊'))
# print(f'集合的内容：{mylist}，他的有{len(mylist)}个元素')

mylist = [1, 3, 5, 11, 1, 3, 8, 7, 6]
def while_iterator():
    index = 0
    while index < len(mylist):
        item = mylist[index]
        print(item)
        index += 1

while_iterator()