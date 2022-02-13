# 列表 字典
# 列表：存储多个数据，获取单个元素，可读性不强，获取每一个时使用索引
# 字典：存储多个数据，获取单个元素，根据标记位key获取
# 非序列，没有顺序，不可以进行索引和切片
# 可变类型，增删改
# key是不可变类型，必须唯一
wumeng = ['吴梦','女',18,'西游记','还珠格格','李白']
# 获取不记得，列表劣势，无标记位
print(wumeng[4])
# 字典，有标记位 key:value
# 表示方法，{key:value,key2:value2}
wumeng = {"name":"吴梦","age":"18","favor_tv":"西游记","gender":"女","most":"还珠格格"}
# 获取某个元素，和列表获取索引差不多
age = wumeng["age"]
print(age)
# 字典表示dict{key:value}
# 不可变类型，key唯一，list不可作为key
# 字典，列表可变  字符串，元组不可变，一般使用字符串作为key
# 唯一，key重复时只取一个
yuz = {"name":"yuze","age":15,"name":"帅哥"}
print(yuz["name"])
print(yuz)
# 获取长度
print(len(yuz))
# 字典是无序的数据类型无索引，列表list是有序的，有索引
# python3.6 第一次打印和第二次打印可能不一样
# python3.7后是按照添加顺序显示
print(yuz)
# 内存当中，列表的数据是存储在一起的
# 字典的key，value存储不同位置
# 字典是可变类型，增删改
# 添加字典元素
# key不可变，value可变
yuz["star"] = ["周杰伦","五月天"]
print(yuz)
# 元素修改
# 1.字典里面双引号单引号没有区别，自动使用单引号
# 2.使用元素修改和元素添加的方式是一样的
# 当key不存在时是添加元素，当key存在时，是修改
yuz["star"] = "小雪"
print(yuz)
# 随机删除
# yuz.popitem()
# print(yuz)
# 指定删除
yuz.pop('age')
print(yuz)
# 其他的方法，清除clear
# yuz.clear()
# print(yuz)
# 字典常用函数
print(yuz.items())
print(yuz.keys())
print(yuz.values())

# 1.无序的，可变类型
# 2.key唯一，不可变类型，value,随意
# 3.增删改，跟列表差不多
# 4.items(),keys(),values()


# TODO：python基础，字典：字典时一系列键值对，每个key与一个value对应，可以使用key来访问键值，与键相关联的值可以是数、字符串、列表乃至字典
# 1.访问字典中的值
alien = {'color':'green','points':'5'}
# 射杀外星人获取分数
new_points = alien['points']
print(f'射杀外星人获得{new_points}分\n')

# 2.添加键值对
# 给外星人添加x轴坐标和y轴坐标
alien['x_position'] = 0
alien['y_position'] = 125
print(alien)

# 3.先创建一个空字典,在空字典中添加键值对有时可以提供便利
alien_0 = {}
alien_0['color'] = 'green'
alien_0['size'] = 'X'
print('\n',alien_0)

# 4.修改字典中的值
alien_0 = {'color':'green'}
print(f"外星人颜色为{alien_0['color']}")
alien_0['color'] = 'yellow'
print(f"外星人颜色变为{alien_0['color']}\n")

# 对一个不同速度移动的外星人进行位置跟踪，为此存储外星人当前速度，并确定该外星人将向右移动多远
alien ={'x_position':0,'y_position':120,'speed':'medium'}
print(f"当前外星人的位置{alien['x_position']}")
# 根据外星人的移动速度将外星人向右移多远
if alien['speed'] == 'slow':
    new_x = 1
elif alien['speed'] == 'medium':
    new_x = 2
else:
    new_x = 3
alien['x_position'] = new_x +alien['x_position']
print(f'外星人向右移动了{alien["x_position"]}')
# 要修改外星人的速度只需修改‘speed’的值即可

# 5.删除键值对：del语句
alien = {'color':'green','size':'x','points':5}
print('外星人信息：',alien)
del alien['size']
print('删掉大小后外星人信息：',alien)

# 6.由类似对象组成的字典
favorite_languages = {
    '周杰伦':'python',
    '王力宏':'java',
    '林俊杰':'c',
}
language = favorite_languages['周杰伦'].title()
print(f'周杰伦最喜欢的语言是：{language}')

# 7.使用get()来访问值
# 使用指定key值来获取值时可能key不存在
alien = {'color':'green','point':5}
# key不存在时报KeyError
# print(alien['size'])
# 可以使用get()来指定key不存在时返回默认值
point_value = alien.get('size','不存在size')
print(point_value)
# key存在时返回value
point_value = alien.get('color','不存在color')
print(point_value)

# 8.遍历字典所有key和value,使用.items()方法
favorite_languages = {
    '周杰伦':'python',
    '王力宏':'java',
    '林俊杰':'c',
}
# 字典items()方法以列表返回可遍历的（键值）元组数组
for name,langue in favorite_languages.items():
    print(f'{name}最喜欢的语言是：{langue}')

# 9.遍历字典所有的key值，使用.keys方法
favorite_languages = {
    '周杰伦':'python',
    '王力宏':'java',
    '林俊杰':'c',
}
# keys()也可以省略，不写时默认遍历字典的key
for name in favorite_languages.keys():
    print(name)
if '华晨宇' not in favorite_languages.keys():
    print("没有华晨宇喜欢的语言")

# 9.按特定顺序遍历字典中的所有键
nums = {'a':1,'c':3,'b':2}
# 使用sorted(key,reverse=)函数进行排序
for num in sorted(nums.keys(),reverse=False):
    print(num)

# 10.遍历字典中所有value
nums = {'a':1,'c':1,'b':2}
for num in nums.values():
    print(num)
# 当value中有相同值需要去重时可以使用set()集合来去重
for num in set(nums.values()):
    print(num)

# 字典嵌套：字典存储列表中
aliens = []
# 创建30个外星人
for alien_number in range(30):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)
# 对前三个外星人修改颜色速度
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 3
        alien['speed'] = 'medium'
# 对前五个中的后两个进一步修改
for alien in aliens[:5]:
    if alien['color'] == 'green':
        alien['color'] = 'red'
        alien['points'] = 8
        alien['speed'] = 'quick'
print(f'前五个外星人是什么样子：')
for alien in aliens[:5]:
    print(alien)
print(f'共有{len(aliens)}个外星人')

# 嵌套：列表存储字典中
pizza = {
    'size':10,
    'toppings':['葱','孜然','胡椒'],
}
print("加了哪些调料：")
for topping in pizza['toppings']:
    print("\t",topping)

# 不同人喜欢多种语言，将用户喜欢的语言依次打印出来
favorite_languages = {
    'ada':['c','java','c++'],
    'bob':['c'],
    'carry':['java','c'],
}
for name,langues in favorite_languages.items():
    if len(langues) == 1:
        print(f'{name.title()}最喜欢的语言只有：{langues[0]}')

    else:
        print(f'{name.title()}最喜欢的语言分别是：')
        for langue in langues:
            print(f'\t{langue}')

# 字典中存储字典:每个用户名作为key,用户信息为value
users = {
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton',
    },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris'
    },
}
for username,userinfo in users.items():
    print(f'\nUsername is :{username}')
    full_name = f'{userinfo["first"]} {userinfo["last"]}'
    location = f"{userinfo['location']}"
    print(f"\t用户的全名是：{full_name.title()}")
    print(f"\t住址是：{location.title()}")
