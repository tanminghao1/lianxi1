# 函数参数
def dalao(name, money, food):
    print("恭喜{}拿到了一个{}的offer.".format(name, money))
    return


dalao('李七七', '18', '辣条')
# 函数的定义和函数的调用，参数要一一对应
# 形式参数要赋值 = 实际参数
# 形式参数和实际参数是一个萝卜一个坑
# 位置参数：形式参数和实际参数要根据位置顺序一一赋值
dalao('辣条', '18', '李七七')

# 关键字参数
# 默认参数
# 位置参数的问题：要求严格，一旦参数多了不好排序

# 贴个标签，关键字参数
# 关键字参数的好处：1.可以换顺序 2.可以部分作为关键字参数
dalao(name='小马哥', money='20', food='海鲜')
dalao(food='海鲜', name='小马哥', money='20')

dalao('小马哥', money='20', food='海鲜')


# 关键字参数必须放到位置参数的后面，否则报错
# dalao(money = '20',food = '海鲜','小马哥')

# 默认参数：作用在于可以少传参数
def dalao(name, money, food='冰激凌'):
    print("恭喜{}拿到了一个{}的offer.".format(name, money))
    print('{}最喜欢吃{}'.format(name, food))
    return


# 当函数定义的时候有默认参数，那么在调用的时候，这个具有默认参数可以不传实际参数，使用默认参数作为实际参数
# 可以少传参数了
# 函数在定义的时候可以复杂，在调用的时候要简单好记，少传参数
dalao('阿花', '25k')


# 默认参数也必须放到位置参数的后面
# 默认参数和关键字参数的区别：
# 默认参数是对于形参，函数定义的时候，关键字参数是对函数的调用


# 传递参数
# 1.位置实参：调用函数时必须将函数调用的每个实参都关联到函数定义中的一个形参，为此最简单的关联方式是基于实参的顺序
# 显示宠物种类和名字
def describe_pet(animal_type, pet_name):
    """
    显示宠物信息
    :param animal_type:
    :param pet_name:
    :return:
    """
    print(f"I have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name}")


# 多次调用函数
describe_pet("猫", "胖喵")

# 位置参数的顺序很重要
describe_pet("朵朵", "猫")

# 2.关键字实参：在实参中直接将名称和值关联起来，一一对应，无需考虑实参顺序
describe_pet(animal_type="cat", pet_name="朵朵")
describe_pet(pet_name="朵朵", animal_type="cat")


# 3.默认值：编写函数时可给形参指定默认值，如果没有传实参，就使用默认实参
# 默认实参在非默认实参后
def describe_pet(pet_name, animal_type="cat"):
    print(f"I have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name}")


# 不传实参时使用默认实参
describe_pet(pet_name="胖喵")
# 如果传了实参，就不使用默认参数
describe_pet(pet_name='朵朵', animal_type='猫')

# 等效的函数调用：位置参数、关键字参数、默认参数
describe_pet("胖喵")
describe_pet(pet_name="朵朵")

describe_pet(pet_name="朵朵", animal_type="猫")
describe_pet("胖喵", "猫")


# 避免实参错误
# describe_pet()
# 编写一个函数，接受一个尺码以及要印到T上的字，将尺码和字打印出来
def make_shirt(size, title):
    print(f"你选了件{size}号的衣服，并印上{title}")


# 使用位置参数调用
make_shirt("大", "‘我爱老婆’")
# 使用关键字参数调用
make_shirt(size='中', title='“爱老婆”')


# 修改函数，默认印“我爱老婆”
def make_shirt(size, title='我爱老婆'):
    print(f"你选了件{size}号的衣服，并印上{title}")


make_shirt("小")
make_shirt(size="加大")


# 编写一个函数，打印城市及属于的国家，设置默认国家，输出非默认国家
def describe_city(city, country='中国'):
    print(f"{city}是属于{country}的")


describe_city("台湾")
describe_city(city="香港")
describe_city("纽约", "中国")
describe_city(city="洛杉矶", country="美国")


# 4.返回值：函数并非总是直接显示输出，它还可以处理一些数据，并返回一个或一组值
# 1.返回简单值
def return_fullname(firstname, lastname):
    fullname = f"{firstname} {lastname}"
    return fullname


full_name = return_fullname("jay", "chou").title()
print(full_name)


# 2.让实参变成可选的：有时需要让实参变成可选的，这样使用函数的人就能在必要时提供额外的信息
# 给形参指定一个空的默认值：=None
def return_fullname(firstname, lastname, middlename=None):
    if middlename:
        full_name = f"{firstname} {middlename} {lastname}"
    else:
        full_name = f"{firstname} {lastname}"
    return full_name


fullname = return_fullname(firstname="j", middlename="J", lastname="Lin").title()
print(fullname)
fullname = return_fullname(firstname="j", lastname="lin").title()
print(fullname)


# 3.返回字典：函数可返回任何类型的值，包括列表、字典等复杂的数据结构
def build_person(first_name, last_name):
    """返回一个字典，其中包含一个人的信息"""
    person = {"first": first_name, "last": last_name}
    return person


musician = build_person("谭", "铭昊")
print(musician)


# 对函数添加年龄、兴趣职业等可选值
def build_person(first_name, last_name, age=None, hobby=None, work=None):
    person = {"first": first_name, "last": last_name, "age": age, "hobby": hobby, "work": work}
    return person


musician = build_person("谭", "铭昊", "28", "看电影", "IT")
print(musician)


# 4.结合使用函数和while循环
def hello(firstname, lastname):
    fullname = f"{firstname}  {lastname}"
    return fullname.title()


# 这是一个无限循环
# while True:
#     print("\n Please tell me your name:")
#     f_name = input("请输入你的姓：")
#     l_name = input("请输入你的名：")
#     formatted_name = hello(f_name, l_name)
#     print(f"\nHello,{formatted_name}")
#


# 告诉用户输入“q”时退出循环
def hello(firstname, lastname):
    fullname = f"{firstname} {lastname}"
    return fullname


# 让用户主动退出循环
# while True:
#     print("\n Please tell me your name:")
#     print("(enter 'q' at any time to quit)")
#     f_name = input("请输入你的姓：")
#     if f_name == "q":
#         break
#     l_name = input("请输入你的名：")
#     if l_name == 'q':
#         break
#     formated = hello(f_name, l_name)
#     print(formated)


# 编写一个函数city_country()的函数，输入城市国家后打印名片
def city_country(city, country):
    print(f"""
--------------------------
    "{country},{city}"
--------------------------
    """)


print(city_country("上海", "中国"))


# 5.传递列表,向函数传递列表
def users(names):
    for name in names:
        msg = f"Hello,{name}".title()
        print(msg)

usernames = ["jay chou", "j j lin", "curry"]
users(usernames)

# 6.在函数中修改列表
unprinted_designs = ['phone case','robot pendant','dodecahedron']
completed_models = []
while unprinted_designs :
    unprinted_design = unprinted_designs.pop()
    completed_models.append(unprinted_design)
    print(f"正在打印：{unprinted_design}")
print("\n这些设计已经打印了：")
for completed_model in completed_models:
    print(completed_model)

# 将程序简化定义为两个函数进行调用
def unprinted_des(unprinted_designs,completed_models):
    while unprinted_designs:
        unprinted_design = unprinted_designs.pop()
        completed_models.append(unprinted_design)
        print(f"正在打印：{unprinted_design}")
def completed_mod(completed_models):
    print("\n这些设计已经打印了：")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case','robot pendant','dodecahedron']
completed_models = []
unprinted_des(unprinted_designs,completed_models)
completed_mod(completed_models)
print(f"原列表：{unprinted_designs}")

# 7.禁止函数修改列表：使用切片创建一个副本进行参数传递，不影响原有列表
unprinted_designs = ['phone case','robot pendant','dodecahedron']
completed_models = []
unprinted_des(unprinted_designs[:],completed_models)
completed_mod(completed_models)
print(f"原列表：{unprinted_designs}")

# 练习1：创建包含多个文本信息的列表，传递给函数打印每条文本信息
txts = ["我爱潇潇","潇潇爱我","潇潇喜欢吃海鲜"]
def print_txt(txts):
    for txt in  txts:
        print(txt)
print_txt(txts)

# 练习2：编写一个函数send_messages()函数，将每条消息打印并移到sent_messages列表中，调用函数打印两个列表
messages = []
def sent_messages(txts,messages):
    while txts:
        message = txts.pop()
        print(message)
        messages.append(message)
sent_messages(txts,messages)
print(f"\nmessages:{messages}")
print(f"txts:{txts}")

# 练习3：调用函数sent_messages时传递txts的副本，使txts列表不被更改
txts = ["我爱潇潇","潇潇爱我","潇潇喜欢吃海鲜"]
messages = []
sent_messages(txts[:],messages)
print(f"\nmessages:{messages}")
print(f"txts:{txts}")

