# 什么是函数
# y = x + 1 ==> f(x) = x + 1
# python:f(x) = x + 1
# x,自变量
# python:x叫做参数，x+1,返回值
# x：输入... ，x+1 return返回值

# python 定义函数
# def add(x):
#     # x 是参数，输入
#     y = x + 1
#     # return就是返回
#     return y
# result = add(2)
# print(result)
# print:将某一个值打印到屏幕上
# return 函数输出的结果，使用变量接收函数的返回值
"""
def 函数名称(参数1，参数2，参数3):
    (缩进)函数体
    函数体里面的内容函数外面看的到吗？？看不到
    外面能看到的（函数名，参数值（输入），返回值（输出））
    return返回值
"""

"""文档字符串，docsting,函数的注释"""
# def swap(x,y):
#     """
#     交换值
#     :param x:
#     :param y:
#     :return:
#     """
#     c = y + 1
#     # 返回的是元组（c,x），也可返回{"a":c,"b":x}
#     return c,x
# print(swap(6,9))

name = 'yuz'
age = 18
gender = '女'
# # 打印名片
# print("""******""")
# print("""名字：{}""".format(name))
# print("""年龄：{}""".format(age))
# print("""性别：{}""".format(gender))
# print("""******""")
# 函数的作用，存储一段可以重复执行的程序,逻辑，可以重复调用
# 1.程序的使用更加简洁，可重复使用
# 2.代码具有可读性，一读函数名称和注释就知道这段代码的作用

# 变量的作用存储数据，函数的作用存储程序，逻辑
def User_Info(name,age,gender):
    """
    打印名片
    :param name:姓名
    :param age: 年龄
    :param gender: 性别
    :return: 默认返回None
    """
    print("""******""")
    print("""名字：{}""".format(name))
    print("""年龄：{}""".format(age))
    print("""性别：{}""".format(gender))
    print("""******""")
    # return None   #省略隐藏返回None
# name = 'yuz'
# age = 18
# gender = '女'
# User_Info()
fact_name = 'tt'
fact_age = 20
fact_gender = '男'
# 参数传递给函数
User_Info(fact_name,fact_age,fact_gender)

my_list = [1,3]
b = my_list.append("hello")
print(b)   # 返回为None，因为append函数中未返回值，所以默认为None
c = my_list.pop(1)
print(c)   # 因为pop()函数中return了my_list[1]，所以被c接收
# 函数的定义的参数和实际传入的参数要相等，且顺序相等
# 函数定义的参数：形式参数，x,y,z
# 函数调用，使用的参数，实际参数，实际的值：1,2,3

# 1.什么是函数，函数的定义和调用 TODO：函数体里面的内容只有当函数被调用时才会被执行
# 2.函数的作用
# 3.return

# 函数基础
#1.定义一个函数
def greet_user():
    """显示简单的问候语"""
    print("Hello!")
# 调用函数可依次指定函数名以及用圆括号括起必要信息，由于无需传递参数，直接输入greet_user()即可
greet_user()

# 2.向函数传递信息：定义一个参数，在调用时传递
def greet_user(username):
    print(f'Hello,{username.title()}!')
greet_user('jay')

# 3.实参和形参
# 在定义函数greet_user(username)时括号内username为形参，在调用函数greet_user('jay')传的值‘jay’为实参，赋值给形参进行使用
def display_message():
    print("本章学习什么是函数")
display_message()

def favorite_book(bookname):
    print(f"My favorite book is '{bookname}'")
favorite_book(bookname='剑来')
favorite_book('仙逆')