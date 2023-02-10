'''
    for循环中的临时变量，其作用域限定为循环内

    python虽然允许 此变量访问，但是不符合规定。
'''

name = '胶税大讲堂'
for char in name:
    print(char);

print(char) # 能访问到，但是不建议这么写