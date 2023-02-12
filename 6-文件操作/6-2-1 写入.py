"""
1. 打开文件
2. 写入文件
3. 刷新flush 表示我们写入的数据让他从内存中 刷新到磁盘真正的文件中，批量写入效率更高。
4. close
"""
# w模式表示是 写入（编辑） 需要进行r模式写入的演示. w模式下 文件存在会覆盖，文件不存在就自动创建

# 1. 打开文件
file = open('D:\\python实训\\6-文件操作\\write_demo.txt', 'w', encoding='UTF-8')
# file = open('D:/python实训/6-文件操作/writedemo.txt', 'w', encoding='UTF-8')
# 2. 写入 write
file.write("123444啊啊啊啊啊啊啊啊啊啊啊啊啊")
# 3. 刷盘
# file.flush() # 当我们调用close的时候，w模式下 python会自动进行flush的动作~
# 4. close关闭
file.close()

# time.sleep(111111111111)

# 反复运行的话会发现会把之前的数据删除~

# with open as语法
# with open('D:\python实训\\6-文件操作\\writedemo.txt', 'w', encoding='UTF-8') as file:
#     file.write('ffffffffffffff')
