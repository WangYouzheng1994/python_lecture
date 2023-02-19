
# print(type({1, 3, 5, "", 1, 3, 5, False, 'asdf'})) # 不重复，不保证顺序

set1 = {1, 3, 5, 7}
set2 = {2, 3, 9}

result = set1.difference(set2)
# print(result)
# print(set1)
# print(set2.difference(set1))
# set1.difference_update(set2)
#
# print(set1)

print(set1.union(set2))
