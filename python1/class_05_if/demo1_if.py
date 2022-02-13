# if语句

# a = 1
# print(type(a))

# 如果a的类型是整形，打印我是大佬
# 如果a的类型是float，打印我是菜鸟
# 否则打印我要学python


# if...elif..else..
# python遇到冒号:要缩进
# if (条件表达式):
    # 条件语句
# elif (另外的条件)：
a = 1
# if..elif..else只会进入符合条件的，其他的分支不会执行
# if (type(a) == int and 'hello' == 'hello'):
#     print("我是大佬")
# elif type(a) == float:
#     print("我是菜鸡")
# elif type(a) == str:
#     print('字符串')
# # 剩下的所有情况
# else:
#     print("我要学python")

# if type(a) == int:
#     print("大佬")
#     if a == 1:
#         print("菜鸟")
#     else:
#         print("学")
#         if a == 4:
#             print("嘻嘻")
# pass 冒号后语句块里不想执行任何东西
if a ==1:
    pass    #后面语句不允许
else:
    print("pass")
print("end") # 执行第一个if对应


# TODO：python基础：if语句
# 示例：对于大多数汽车品牌首字母大写方式打印其名，对于’bmw‘，应以全大写打印
cars = ['audi','bmw','benz','toyota','nisan']
for car in cars:
    if car == 'bmw':
        print(f'车名大写：{car.upper()}')
    else:
        print(f'车名首字母大写：{car.title()}')

# 1.简单的if语句
age =40
if age >= 18:
    print('已成年')
# 2.if-else语句
if age < 18:
    print('未成年')
else:
    print('已成年')
# 3.if-elif-else:4岁以下免费，4-18岁半价，18岁以上全票
if age < 4:
    price = 0
elif age < 18:
    price = 20
else:
    price = 40
print(f'你需要交{price}元门票钱')
# 4.使用多个elif
if age < 4:
    price = 0
elif age < 18:
    price = 20
elif age > 60:
    price = 0
else:
    price = 40
print(f'你需要交{price}元门票钱')
# 5.省略else
if age < 4:
    price = 0
elif age < 18:
    price = 20
elif age >= 60:
    price = 0
print(f'\n你需要交{price}元门票钱')

# 测试多个条件
requested_toppings = ['盐','鸡精']
if '盐' in requested_toppings:
    print('需要加盐')
if '鸡精' in requested_toppings:
    print('需要加鸡精')
if '酱油' in requested_toppings:
    print('需要加酱油')

# 檢查特殊元素
requested_toppings = ['盐','鸡精','酱油']
for requested_topping in requested_toppings:
    if requested_topping == '鸡精':
        print('没有鸡精了')
    else:
        print(f'加{requested_topping}')
print('披萨制作完成')

# 确定列表不是空的
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f'加{requested_topping}')
    print('披萨制作完成')
else:
    print('\n要原味的吗\n')

# 使用多个列表，示例：店内调味表和用户点的调味，当用户点的有时添加，没有时告诉顾客没有
available_toppings = ['花椒','辣椒粉','香菜','香油','葱花','蒜']
requested_toppings = ['香菜','葱花','蒜']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f'可以加{requested_topping}')
    else:
        print(f'没有{requested_topping}了')
print('马上给您制作披萨\n')
'''
作业：创建一个至少包含5个用户名的列表，且其中一个为admin,想像你要编写代码，在每位用户登录网站
后打印一条问候消息。遍历用户列表，并向每位用户打印一条消息
'''
# 1.如果用户名为’admin‘，打印一条特殊问候消息,否则打印普通消息
users = ['a','b','c','admin','d']
for user in users:
    if user == 'admin':
        print(f'热烈欢迎{user}')
    else:
        print(f'你好，{user}')
# 2.检查用户为空的情形，如果为空打印：我们需要一些用户
users = []
if users:
    for user in users:
        if user == 'admin':
            print(f'\n热烈欢迎{user}')
        else:
            print(f'你好，{user}')
else:
    print('\n我们需要一些用户\n')

# 3.如何确保注册用户名唯一
current_users = ['AA','Bob','Cyi','Dd','Jj']
# 列表解析,将原列表字符串转化为小写存储在新的列表
current2 = [current_user.lower() for current_user in current_users if isinstance(current_user,str)]
new_users = ['Bob','DD','Cy','kk','mm']
for new_user in new_users:
    if new_user.lower() in current2:
        print(f'{new_user}名字已存在')
    else:
        print(f'可以注册{new_user}')

# 4.在一个列表中存储1-9，用序数打印，如：1st,2nd,3rd,4th,5th,6th,...,10th
nums = [1,2,3,4,5,6,7,8,9,10]
for num in nums:
    if num == 1:
        print(f'{num}st')
    elif num == 2:
        print(f'{num}nd')
    elif num == 3:
        print(f'{num}rd')
    else:
        print(f'{num}th')