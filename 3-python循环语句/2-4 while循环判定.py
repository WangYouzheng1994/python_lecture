'''
只要条件满足 就会无限循环
'''
i = 0
while i < 100: # 这里也是 boolean 判定，只要是true就会一直循环执行
    print(f'目前执行到了, {i}')
    i += 1
else: print('我结束了哈')