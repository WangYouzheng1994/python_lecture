'''

    引入一个新的概念，函数和方法的区别。

    我们之前定义的
    def xxx_func(a):
        print(a)
    xxx_func('a')
    xxx_func 称之为一个函数

    方法是写在对象里面的

    提前引入面向对象的概念
    讲解堆栈内存的模型
'''

# 1. 查找某个元素是否存在
list = ['小狗', '小猫', '小老虎']

# print(list.index('狗狗~')) 出现ValueError异常，程序终止了

print(list.index('小老虎'))

# 2.修改指定位置（索引）的元素值
list[1] = '小猫~~~'

print(list)
list[-2] = '猫'
print(list)

# 3. 插入元素 insert(从第几个进行插入, 插入的元素)
list.insert(1, 123) # 插入新值，从第一个值开始插入，123
list.insert(40, '乌龟') # 从第40个开始插入，但是目前最大值5
print(list)

# 4. 末尾追加 append(元素)
list.append("我是第一个")
list.append("我是第二个")
print(list)

# 5. 末尾追加一批元素（数据容器）
last_list = ["我是追加容器的第一个值", "我是追加容器的第2个值", "我是追加容器的第3个值"]
list.extend(last_list) # 把last_list 追加到list最后

print(list)

""" 6. 移除元素 del list[1] 删除list列表的第二个元素
        移除元素 pop(下标)
"""
# del语法
del list[1]
print(list)
pop_var = list.pop(4) # pop相当于弹出。。有返回值，为了实现出栈（数据结构概念）与队列用的
print(f"list集合，pop出来的元素是：{pop_var}")

# 7. 删除某元素在列表中的第一个匹配项 列表.remove(元素)
list.append("1")
list.insert(4, "1")
print(list)

list.remove("1")
print(list)

# 8. 清空列表
list.clear();
print(list)

# 9. 统计列表内某元素的数量 count(元素)
last_list = [1,2,3,3,4,1,5]
list.extend(last_list)
print(list)
print(list.count(1))

# 10. 统计列表中全部元素数量，很重要~ len(列表对象)
print(len(list))