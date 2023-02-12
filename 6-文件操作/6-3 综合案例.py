"""
读取一个文件并写入一个新文件，
新文件的要求：
    将你好替换为hello，
    将,号替换为 空格。
    将@符号丢弃
    将ttt开头的行丢弃
    将bb结尾的追加CC

    https://www.runoob.com/python/python-strings.html
"""
target_file = open('D:\\python实训\\6-文件操作\\6-3 综合案例\\t_demo.txt', 'w', encoding='UTF-8')
# with open as语法
# 相对路径 with open('/6-文件操作/6-3 综合案例\\source_demo.txt', 'r', encoding='UTF-8') as file:
# 绝对路径，从盘符开始D:\python实训\6-文件操作\6-3 综合案例\source_demo.txt
iter_num = 0
with open('D:\\python实训\\6-文件操作\\6-3 综合案例\\source_demo.txt', 'r', encoding='UTF-8') as file:
    for line in file:
        # 截取
        if line[0:3] == 'ttt':
            continue
        # 将 你好替换为hello，
        new_line = line.replace('你好', 'hello')
        # 将,替换为 ，
        new_line = new_line.replace(',', ' ')
        # 将,@删除 ，
        new_line = new_line.replace('@', '')
        # 去掉读取到的换行符 # lstrip left左边的进行strip
        new_line = new_line.rstrip('\n')
        # 你好bb\n
        if new_line.endswith('bb'):
            # 你好bbCC
            new_line += 'CC'

        new_line += '\n'  # 把替换掉的换行符补充回去
        target_file.write(new_line)
    target_file.write("我写完了~~~")
# 关闭目标并且刷新写入
target_file.close()
