"""
文件编码技术：
1.常见的文件编码字符集有：UTF-8（支持中文），GBK（中文，支持的字儿更多），BIG5（繁体字更多）
2.编码、解码的目的是：将人类能看懂的字符或者数据与计算机能看懂的数据（0，1）进行互转
互转的基础就是 编码字符集。编码字符集中存储了所有明文与对应的二进制信息。
3.UTF-8是全球最通用的编码字符集，如果没有特殊要求一律使用UTF8（约定优于配置）
4. 演示：打开windows的记事本 看右下角是有UTF-8 这个说明的
5. 字符和字节的关系是：一个英文字符等于一个字节，一个中文字符(含繁体)等于三个字节。
这里的字节是一个存储大小的单位英文是 byte，一个字节是8比特（bit）
6. 为什么中文要占用三个字节？？ 简单理解，中文每个字都要用独立的二进制码表示，字多啊，所以要占用的就多。
"""
# 1. 打开文件 open(name目标文件路径, mode访问模式, encoding解析文件的字符集)
# 访问模式：
#     'r'       open for reading (default)
#     'w'       open for writing, truncating the file first
#     'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
file = open('/基础部分/6-文件操作/read.txt', 'r', encoding='UTF-8')
print(file)
print(type(file))  # I/O操作对象是所有开发语言都会进行涉及的要点即：input和output，是相对于内存与磁盘来描述的

# 2. read() 读取文件
print(file.read(5)) # 表示读取五个字符
print(file.read(5)) # 又读取了5个，发现他自己继续往后了，是不是很像游标啊~
print(file.read()) # 读取所有

# 3. readlines() 读取全部行封装到list列表，如何判定的一行？Windows是'\r\n',Linux是'\n' pycharm的是 \n
print(file.readlines())  # 读取的内容为什么有个\n? 解答：所有\n, \r, or \r\n被默认转换为\n

# 4. readline()#读取一行
print(file.readline())  # 读取一行
print(file.readline())  # 读取一行
print("str\n")
print("str")

# 5. 使用for循环读取文件，避免撑爆内存与延迟
for line in file:
    print(f'当前行数据为：{line}')

# 6. 关闭文件 close
# 举例子：如果我们同时打开一个word 她会提示被占用。
# 我们操作完文件需要进行关闭，否则文件会被python一直占用。close他也会释放对应的资源
file.close()


'''
open
read/readline
close


'''