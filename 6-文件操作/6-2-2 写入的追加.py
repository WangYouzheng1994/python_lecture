"""
使用a模式
文件存在就追加
文件不存在就创建并进行写入
\n
"""
# 1.打开
file = open('D:\python实训\\6-文件操作\\writedemo1.txt', 'a', encoding='UTF-8')
# 2. 写入
file.write('1221211AAAAAAAAAAAAA')
file.write('\n你好 这是我追加的行~')
# 3. 刷新 close 自动刷
# file.flush()
# 4. close
file.close()


