"""
1.将用户输入的所有数字相乘之后对20取余数
用户输入的数字个数不确定
"""
# nums = input("请输入数字,用逗号隔开")
# # 保存多个数据，用列表存储
# # 字符串转化成列表，用逗号分割，split
# nums_list = nums.split(',')
# 取余数，逻辑稍微复杂一点的，封装成函数
# 参数：1.列表作为参数 2.不定长参数*args
# def get_mod(*args):
#     product = 1
#     for arg in args:
#         product *= int(arg)
#     return product % 20
# # nums_list是一个列表，函数参数是不定长参数，需要解包
# print(get_mod(*nums_list))
# 函数定义就是一个普通参数，可以直接传一个列表
# print(get_mod(nums_list))

# 什么时候封装函数
# 逻辑比较复杂的时候
# 多个地方同时使用某一段程序
# 1,要不要参数？有参数
# 2,函数封装返回值一般是确定的，根据参数确定的
import random

"""
1.编写函数，检查传入列表的长度，如果大于2，那么仅仅保留前两个长度的内容，并将新内容返回

三元表达式，三目运算
"""


# def remain_two(mlist):
#     if len(mlist) > 2:
#         return mlist[:2]
#     return mlist
#
# print(remain_two([3, 3, 4]))

# 三目运算，三元表达式
# def remain_two(mlist):
#     return mlist if len(mlist) > 2 else mlist

"""
3.定义一个函数，传入一个字典和字符串，判断字符串是否为字典中的值，如果字符串不在字典中，则添加到字典中
并返回新的字典。
加入默认参数的情况，values()
# key保持不可变类型，并且是唯一的
"""


# def add_element(e, mdict={}):
#     if e not in mdict.values():
#         # e作为key
#         while True:
#             key = random.randint(1,999)
#         # 判断key是否在mdict.keys()
#             if key not in mdict.keys():
#                 mdict[key] = e
#                 break
#     return mdict
# print(add_element('eee',{'1':'ef','2':'ff'}))

# key永远不可能重复，时间点作为key
# import time
# int(time.time())

"""
4.通过定义一个计算器函数，调用函数传递两个参数，然后提示选择【1】加【2】减【3】乘【4】除 操作，选择之后返回对应操作的值
"""
# methods = {'1':'+','2':'-','3':'*','4':'/'}
# def calc(x,y,method):
#     # methods['1'] + - * /
#     method_f = methods[method]
#     # 字符串转化成可以运算的python代码
#     return eval("{} {} {}".format(x,method_f,y))
# method = input("请输入运算符：")
# print(calc(3,4,method))

"""
5.一个足球队在寻找年龄在15岁到22岁的女孩做啦啦队（包括15,22,）加入，编写一个程序，询问用户年龄性别，询问10次后，输出满足条件的人数
"""
# def join_team(age):
#     if 15 <= age <= 22:
#         return True
#     return False
# def main():
#     num = 0
#     for i in range(3):
#         age = input("请输入年龄：")
#         if not age.isdigit():
#             print("输入不合法")
#             continue
#         joined = join_team(int(age))
#         if joined:
#             num += 1
#     print(num)
# print(main())
"""
1.将列表cases = [['case_id','case_title','url','data'],['1','用例1','baidu.com','百度']]
转换为{"case_id":"1","case_title":"用例1","url":"baidu.com","data":"百度"}
"""
cases = [['case_id','case_title','url','data'],['1','用例1','baidu.com','百度']]

# def transform(cases):
#     #if type(cases)  != list:
#     # 判断类型
#     if not isinstance(cases,list):
#         return
#     title  = cases[0]
#     new_cases = []
#     for case in cases[1:]:
#         dict_case = {}
#         # enumerate 可以同时获取索引和值
#         for i,colnum in enumerate(case):
#             dict_case[title[i]] = colnum
#         new_cases.append(dict_case)
#         return new_cases
# print(*transform(cases))
# zip()
# title = ['a','b','c']
# value = [1,2,3]
# a = zip(title,value)
# print(list(a))
# zip方法
# def transform_zip(cases):
#     if type(cases) != list:
#         print("输入错误")
#         return
#     new_case = []
#     title = cases[0]
#     for i in cases[1:]:
#         new_dict = dict(zip(title,i))
#         new_case.append(new_dict)
#     return new_case
# print(*transform_zip(cases))

# def filter(cases,id):
#     new_cases = []
#     for c in cases:
#         if c['case_id'] > id:
#             new_cases.append(c)
#     return new_cases
