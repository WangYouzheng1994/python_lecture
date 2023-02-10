# 定义一个元祖，对其填充进不同类型的数值，必须要有list
# 对其进行 下标取值操作、查询指定数据、删除list的指定数据、增加list指定的数据
inside_list = [1, 3 ,5]
var_tuple=(1, 2, "3", False, 4.4, inside_list)
#取值
print(var_tuple[0])
# 查询
print(var_tuple.index(inside_list))
# print(var_tuple.index(inside_list)) #报错

# 删除内部数据 1
var_tuple[var_tuple.index(inside_list)].remove(1)
print(var_tuple)
# 增加内部数据
var_tuple[var_tuple.index(inside_list)].append('我是新的')
print(var_tuple)