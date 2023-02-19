'''
读取一个windowsread.txt文件，并且 识别出字符串'你好'的出现次数
'''
str_count = 0
with open('/基础部分/6-文件操作/windowsread.txt', 'r', encoding='UTF-8') as file:
    for line_str in file:
        print(f'当前行是：{line_str}')
        str_count += line_str.count('你好')


print(f'\'你好\'的出现次数是：{str_count}')

# 换行的原因是，读取出来以后 每行都有一个换行符\n

# strip的作用 再补充：他可以去掉\n换行~

str_count = 0
with open('/基础部分/6-文件操作/windowsread.txt', 'r', encoding='UTF-8') as file:
    for line_str in file:
        print(f'当前行是：{line_str.strip()}') # strip 去掉了换行
        str_count += line_str.count('你好')


print(f'\'你好\'的出现次数是：{str_count}')
