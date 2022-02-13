import random
"""
1.商场降价，价格都是整数，如果购买50-100元打九折，
如果购买大于100元，打8折，编写一程序，询问购买价
格，再再显示折扣
"""
# from decimal import Decimal
# price = int(input("总金额："))
# # price_after = price
# # 类型是什么，字符串
# if 50 <= price <= 100:
#     # 打折以后的价格,Decimal浮点运算精确
#     price_after = price * (1-0.1)
# elif price > 100:
#     price_after = price * (1-0.2)
# else:
#     price_after = price    #如果没有else，price_after没有被定义
# print("实付金额：",price_after)


"""
2.输入一个有效年份，判断是不是闰年
1>普通闰年：4的倍数，但不是100的倍数
2>能被400整除
"""
# year = int(input("请输入年份："))
# if (year % 4 == 0 and year % 100 !=0) or (year % 400 == 0):
#     print("这是一个闰年")
# else:
#     print("这不是一个闰年")

"""
3.使用遍历循环完成剪刀石头布游戏，展示用户输入要出的手，石头（1）、剪刀（2）、布（3）、退出（4）
电脑随机出拳比较胜负，显示用户胜负平，运行如下：
提示：电脑随机出拳
    使用随机数，首先需要导入随机数的模块--“工具包”
    import random
    导入模块后，可以直接在模块名称后面敲一个"."然后按TAB键，会提示该模块中包含的所有函数
    random.randint(a,b),返回[a,b]之间的整数，包含a和b
random.randint(1,10) # 生成的随机数n:1<=n<=10
random.randint(4,4)  # 永远都是4
random.randint(25,12) #语句错误，下限必须小于上限
"""
# while True:
#     # 自己出拳
#     # 电脑出拳
#     # 判断，如果。。情况
#     # 如果。。
#     # 如果。。
#     choice = int(input("请出入猜拳：石头（1）、剪刀（2）、布（3）、退出（4）:"))
#     if choice  == 4:
#         print("退出游戏")
#         break
#     # 电脑出拳
#     pc_choice = random.randint(1,3)
#     if (pc_choice == 1 and choice == 3) or (
#             pc_choice == 2 and choice == 1) or(
#             pc_choice == 3 and choice == 2):
#         print("你赢了")
#         break
#     elif pc_choice ==choice:
#         print("平局")
#         break
#     else:
#         print("你输了")
#         break

"""
3.求三个整数中的最大值
"""
# a = int(input("请输入a的值"))
# b = int(input("请输入b的值"))
# c = int(input("请输入c的值"))
# num = {'a':3,'b':4,'c':1}
# max_num = a
# if a < b:
#     max_num = b
# if max_num < c:
#     max_num = c
# print("最大值为：",max_num)

# 扩展方法
# a = 3
# b = 7
# c = 9
# # 使用max方法
# print(max(a,b,c))

# 排序取最大值
# list_my = [3,8,1]
# # list_my.sort()
# # print(list_my[-1])
#
# # for
# max_num = list_my[0]
# for i in list_my:
#     if i > max_num:
#         max_num = i
# print(max_num)

# 输出九九乘法表，格式如下：（每个等式之间空一个Tab键，可以使用"\t"）
"""
1 * 1 = 1
1 * 2 = 2   2 * 2 = 4
。。。
"""
# for i in [1,2,3,4,5,6,7,8,9]
# num = 0
# while num <= 9
# for i in range(9)
# [0,1,2,...,8]
# range(start(0),end,step(1))
# rang(0,9,1)
# 生成一个数字的类似于列表的东西
# for i in range(1,10):
#     for j in range(1,10):
#         # 如果 j <= i
#         if j <= i:
#             print("{} * {} = {}".format(i,i,i * i),end='\t')
#     print()

# for循环遍历
# for i in range(1,10):
#     for j in range(1,i+1):
#         # 如果 j <= i
#         # if j <= i:
#         print("{} * {} = {}".format(j,i,j * i),end='\t')
#     print()    # 换行

# # 特征
# # range(1,10)
# # 会同时取出两个数字去进行操作，for...for...
# # while
# i = 1
# # 第一个计数器
# while i <10:
#     j = 1
#     # 第二个计数器
#     while j <= i:
#         print("{} * {} = {}".format(j,i,j*i),end='\t')
#         j = j +1
#     # 跳出内循环后换行
#     print()
#     # 外循环自增
#     i +=1
# # 结束外循环后，输出换行
# # print()

"""
1.使用循环去完成排序算法
"""
# [1,5,3,2,7,9],for..for..
# while:..while..

"""
6.你的微信好友中有五个微商，他们存在一个列表["卖茶叶","卖面膜","卖保险","卖花生","卖手机"]
请把这五个人从black_list当中删除，最后black_list为空
"""
black_list = ["卖茶叶","卖面膜","卖保险","卖花生","卖手机"]
# for wx in black_list:   #list删掉第一个后,买面膜的索引变为0，列表长度不断变化，所以后导致删不干净，所以要先复制一个列表出来
#     black_list.remove(wx)
#     # for循环索引默认index+1
# print(black_list)

# 通过切片复制一个列表出来

# for wx in black_list[:]:    # 通过切片或者copy的方式复制一个list出来,保证列表不变，索引不变
#     black_list.remove(wx)   # 删除的是上面全局定义的list
# #     index+1
# print(black_list)

# 字符串的
# 复制
# # b = black_list    字符串可以这么写，列表应该用切片方式
# b = black_list[:]
# black_list_new = black_list
# for wx in black_list:    # 一样的删不干净，因为black_list_new跟着black_list变化
#     black_list.remove(wx)
# print(black_list)

# 总结，for循环里面修改列表
# 以后千万不要在for循环中修改列表
# 如果要修改，要copy列表

# 第二种方式，每次索引不变，删除第一个
# for wx in black_list:      #只执行了三次循环，有五个元素，还是删不干净
#     black_list.pop(0)
# #     index+1 此时原来的list[1]变为0，wx取的是更新后的list[1]不是list[0]
# print(black_list)

while len(black_list) > 0:    #用外循环不断循环
    black_list.pop(0)
print(black_list)