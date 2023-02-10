'''
range() 函数去生成一个数字序列


'''

# 从0开始生成到5
for int in range(5):
    print(f"range（5）: {int}")

# 从5开始生成到10，包头不包尾，左闭右开
for int in range(5, 10):
    print(int)

# 从11开始 步进2 生成到15
for int in range(11, 15, 2):
    print(int)

