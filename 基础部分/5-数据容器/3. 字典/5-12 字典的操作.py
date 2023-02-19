myDict = {'1': '张三', '2':'李四', '1': '王五'}
# 新增  xx[key]=value
myDict['555'] = 555555555
print(myDict)
# 更新
myDict['555'] = 66666
print(myDict)
# 删除 并返回元素
print(myDict.pop('555'))
print(myDict)
# 清空
myDict.clear()
print(myDict)
# 获取全部的key
myDict = {'1': '张三', '2':'李四', '1': '王五'}
print(myDict.keys())
print(type(myDict.keys()))

# 遍历 遍历 keys 来获取
for key in myDict.keys():
    print(myDict[key])
# 遍历2，不用非得根据keys获取了 直接遍历 字典 拿到的就是key
for key in myDict:
    print(myDict[key])

# 统计数量
print(len(myDict))