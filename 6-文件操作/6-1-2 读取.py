# 使用with open() as 来读取文件 ： 他可以实现自动close() 解除文件的占用
with open('D:\python实训\\6-文件操作\\windowsread.txt', 'r', encoding='UTF-8') as file:
    for line_str in file:
        print(f'当前行是：{line_str}')