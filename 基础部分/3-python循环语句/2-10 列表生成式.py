'''
python 列表生成式
https://blog.csdn.net/wei18791957243/article/details/108026789

注意：列表生成式相比较普通列表的生成式，比较简洁，
但是只能实现简单的逻辑，否则代码的可读性降低
'''

'''
语法说明：
1.列表生成式：是python内置的比较简单但是功能强大的用于生成list的生成式
 语法：  [元素  for循环  if语句]
说明：   元素和for循环不能省略，但是，if语句可以省略
'''


list_1 = ['hello', 10, 'Abc', 'asBd', True]
# 方式一，传统方案：
newlist_1 = []
for s in list_1:
    if isinstance(s, str):  # isinstance()来判断是不是str类型
        newlist_1.append(s.upper())
print(newlist_1)

# 方式二，列表生成式，仔细看就是lambda的样子~：
newlist_2 = [s.upper() for s in list_1 if isinstance(s, str)]
print(newlist_2)
