"""
    集合（set）的特点：支持去重，且内容无序（插入与取出的顺序不固定），可以多种类型存储，使用for进行迭代
"""

# 定义字面量
{1, 3, 5, "", 1, 3, 5, False}
print() # 不重复，不保证顺序
# 变量
my_set = {1, 3, 5, "", False}
print(my_set)
# 空
empty_set = set()
print(empty_set)

# 因为无序，所以没有下标

########## 集合的操作 #######
# 新增元素
empty_set.add("第一个")
empty_set.add("\"222\"")
print(empty_set)

# 删除元素
empty_set.remove("第一个")
print(empty_set)

# 随机获取一个
print(empty_set.pop())
# 元素会被取出并且从set中移除
print(empty_set)

# 清空
empty_set.add("sadfdasf")
print(empty_set)
empty_set.clear()
print(empty_set)

# 差集 集合1 减掉 集合2中双方共有的，
set1 = {1, 3, 5, 7}
set2 = {2, 3, 9}

result = set1.difference(set2)
print(result)
print(set2.difference(set1))

# 求差 并且不生成新集合而是改变原来的集合
print(set1.difference_update(set2)) # 没有返回值，
print(set1) # 把set1中和set2 重复的元素给删掉了

# 集合合并出新的集合
print(set1.union(set2))
# 统计某元素的个数 len
print(len(set1))