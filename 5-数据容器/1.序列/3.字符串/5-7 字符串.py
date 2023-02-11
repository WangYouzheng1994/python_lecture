# 字符串 其实也是一个数据容器

name = 'abacstrasdb cab '

# 下标取值 0开始
print(name[2])
# index获取指定元素的第一个的下标
print(name.index('a'))

print(name.index('as'))

# replace替换
new_name = name.replace('as', 'bbbbbbb') # as替换为bbbbbbb
print(new_name)
# split切割
new_name = name.split("a")
print(new_name)
# strip 两头去除掉
new_name = name.strip()
print(new_name)

new_name = name.strip('acb') # 他其实是把两头紧连着的字符 只要是匹配到 acb的 就给去掉了
print(new_name)

# 统计某字符串出现的次数
print(name.count("a"))
print(name.count('as'))
# 统计字符串的长度

print(len(name))