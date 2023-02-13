"""
列表使用：[]
元祖使用: (xx,)
字符串使用：""
集合set使用 {}
字典dict用 {xx:xx, }
"""
# 通用转换
#list(容器)、str(容器)、tuple(容器)、set(容器)
# 共同的方法len(), max() min()
mystr = '12345' # 字符串
mylist = [1,2,3,45] # 列表
mytuple = (12,2,3,4,5) # 元祖
myset = {1,2,3,4,5} # 集合
# 正序 升序
print(sorted(mytuple))
# 倒叙 降序
print(mytuple)
print(sorted(mytuple, reverse=True))


"""
数据容器分为可变与不可变类型：
    1. 可变类型：
    2. 不可变类型：

"""
