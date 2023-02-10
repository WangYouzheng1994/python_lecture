# while循环迭代
t8 = ("啊", 123, True, "的", "非")
index = 0
while index < len(t8):
    print(f"元祖的元素有：{t8[index]}")
    index += 1

# for 循环迭代
for element in t8:
    print(f"元祖的元素：{element}")

# 修改内容 (表示 元素不能更改) TypeError: 'tuple' object does not support item assignment
t8[0] = 'aaaaaaa'