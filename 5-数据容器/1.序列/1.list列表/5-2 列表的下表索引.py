'''
    根据下标索引获取数据
'''

# 正向索引的获取
list = [1, 2, 3, 4, 5]

# 正向索引 从小到大， 最小的数是第一个
print(list[0])
print(list[1])
print(list[2])
print(list[3])
print(list[4])
# 反向索引 也是从小到大， 最小的数是第一个
print(list[-1])
print(list[-2])
print(list[-3])
print(list[-4])
print(list[-5])

# 通过下标索引取出对应位置的数据
mylist = ["tom", 'dog', 'ford', 'BenZ']
print(list[0])

# 获取嵌套列表中的元素
mylist = [['dog', 'cat'], ['青岛', "济南", "潍坊", "烟台"], ['山东省', '陕西省', '湖北省', '四川省']]

print(mylist)
print(mylist[0])
print(mylist[0][1])

print(mylist[1][3])

# 超出范围会报错
print(mylist[4])