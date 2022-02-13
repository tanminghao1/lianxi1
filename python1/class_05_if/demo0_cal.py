# 数据运算
# 算数运算，加减乘除
print(1 + 1)
print(900 - 100)
print(100 * 2)
# 除法,python版本最新整除会保留一位小数的float
print(type(900 / 2))

# 整除
print(8 // 3)
# 取余，模运算
print(8 % 5)
# 幂运算
print(2 ** 3)

# 算数运算有个坑
# 浮点数运算 不能精确
# 如果我们要去测试，，100.1-0.2 预期结果99.9，实际不是
# 咋整，怎么解决，避免

from decimal import Decimal
print(100.1 - 0.2)
# Decimal 能够保持很高的精度
# Decimal 函数里接收的是字符串形式，不要写成数字形式
print(Decimal('100.1') - Decimal('0.2'))
print(Decimal('100.1') - Decimal('0.2') == Decimal("99.9"))

# 赋值运算
name = 'yuz'
# +=,-+,*=,/=
name += 'wang'
print(name)
age = 500
age -= 1
print(age)

# 比较运算
# 大于、小于、等于、不等于、大于等于、小于等于
# TODO:等于符号是2个等号 =
# 比较运算得到的结果是布尔值
print(1 == 3-2)
print(4 != '4')

# 逻辑运算 and not or
# and  并且
print(1 == 1 and 2 == 3 )

# or 或者
print(1 == 1 or 2 == 3)   # 只要有一个为真，就是真

# not 非,取反
print(not (1 == 1 or 2 == 3))
# 优先级不去记忆
# 搞不清优先级加括号提高优先级
# 逻辑运算的结果是布尔值true和false
print(not ((1 == 1) or (2 == 3)))

# 成员运算
# in ,not in
print('yuz' in 'yuz wang')
print(3 not in [1,2,3])
# 字典的in是判断key值，不是value
print('name' in {'name':'yuz','age':13})


# TODO：python基础：条件测试
# 1.检查是否相等
car = 'bmw'
print(f"\ncar是否等于bmw:\n\t\t\t{car == 'bmw'}")

car = 'audi'
print(f"car是否等于bmw:\n\t\t\t{car == 'bmw'}")

# 2.检查是否相等时忽略大小写
car = 'Audi'
print(f"\n不区分大小写：{car.lower() == 'audi' }")

# 3.检查是否不相等，使用!=
request_topping = 'mushrooms'
if request_topping != 'anchovies':
    print('\nHold the anchovies!')

# 4.数值比较
age = 18
print(f'\n检查age是否为18：{age == 18}')

if age != 20:
    print("age不等于20")

# 5.检查多个条件，使用and
age_0 = 18
age_1 = 20
if age_0 >=18 and age_1 >=20:
    print('\n两个已成年')
else:
    print("有人未成年")

# 使用or检查多个条件
age_2 = 17
age_3 = 16
if age_2 >= 18 or age_3 >= 18:
    print('有人成年了')
else:
    print('\n都未成年')

# 6.检查特定值是否包含在列表中
request_toppings = ['a','b','c']
request_topping = ['a','c','d']
for req in request_toppings:
    if req in request_topping:
        print('true')
    else:
        print('false')

# 7.布尔表达式
game_active = True
can_edit = True