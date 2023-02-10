'''
    将容器内的元素，依次取出，称之为遍历、迭代
'''
# while 遍历
list = [1,3,5,11,1,3,8,7,6]
def while_iterator():
    index = 0
    while index < len(list):
        item = list[index]
        print(item)
        index += 1

# for 遍历，更简单，不用自己控制下标迭代与终止操作
def for_iterator():
    for item in list:
        print(item)

# while_iterator()
for_iterator()