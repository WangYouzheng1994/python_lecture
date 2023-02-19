'''
range() 函数去生成一个数字序列
'''
# {0, 1, 2, 3, 4}
# 从0开始生成到5
# for my_int in range(5):
#     print(type(my_int))
#     print(f"range（5）: {my_int}")

# 从5开始生成到10，包头不包尾，左闭右开
# for my_int in range(5, 10):
#     print(my_int)

# 从11开始 步进2 生成到15
for my_int in range(11, 15, 2):
    # None
    print(my_int)
else:
    print('over')