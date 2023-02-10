# 给定字符串 中 ： 你好，我是xxx, abc,efg,b ca
# 1 统计出现了多少次"ab"字符
# 2 字符串内的空格，全部进行替换"。"
# 3 使用 "。" 进行字符串分割

str = "你好，我是xxx, abc,efg,bca"

# 1. 统计
print(str.count("abc"))
# 2 替换
str = str.replace(" ", "。")
print(str)
# 3 分割
split_str = str.split("。")
print(split_str)