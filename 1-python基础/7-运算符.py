# 算数（数学）运算符： 加+ 减- 乘* 除/ 取整// 取余% 指数**
print('算数运算 -- START')
print('1+1=', 1 + 1)
a = 1
print('a + a =', a + a)
print('指数:', 3**2)
print('4 / 2 = ', 4 / 2)
print('4 取整 2 = ', 4 // 2)
print('3 取整 2 = ', 3 // 2)
print('4 取余 2 = ', 4 % 2)
print('3 取余 2 = ', 3 % 2)
print('算数运算 -- END')


print('赋值运算符 -- START')
# 赋值运算符： 把 等号有变的结果付给左边的变量
a = 2
a = a + 1 * 2 // 3
print("a + 1 * 2 // 3 = ", a)
print('赋值运算符 -- END')

# 复合赋值运算符 语法糖
'''
+=
a += a 
a = a + a
-=
*=
/=
%=
**=
//=
'''
print('复合赋值运算符 -- START')
a = 1
a += a
print(a) # a = a + a
a += 3 # a = a + 3
print(a)
print('复合赋值运算符 -- END')
