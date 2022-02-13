# while (重点)
# 打印无限次的"我喜欢xx"
# while (条件表达式,当接收表白的时候)
hh = 0
# if ,while
# while (hh < 100):           # True == True
#     print("我喜欢xx")
#     print(hh)
#     hh += 1
# print("hh已经爱我了")

# while True:
#     print("我喜欢xx")
#     if hh == 99:
#         print("xx拒绝了")
#         # break 以后，循环关系结束，退出循环
#         break
#         # 手工终止程序
#     # 退出这个条件，进入下个分支
#     # continue
#     hh += 1
# print("不做舔狗")

#
# my_list = [('本本','海鸥'),('yuz','鱼'),('andy','七七')]
# for name in my_list:         #从索引为0的位置开始循环
#     # 获取的是元组
#     # print(name)
#     # 再获取元组里每一个元组
#     for i in name:
#         print(i)

list_1 = [4,5,6]
list_2 = [2,3,4]
for v1 in list_1:
    # V1 = 4
    for v2 in list_2:
        # v2 = 2
        print("{}+{}={}".format(v1,v2,v1+v2))
        # 隐藏 index2 + 1
    # 隐藏 index1+1

# TODO：while循环简介
# for循环用于针对集合中的每个元素都执行一个代码块，而while循环则不断运行，直到指定条件不满足为止
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# 让用户选择何时退出
# time = ''
# while time != 'N':
#     time = input("你要继续玩游戏吗？请输入Y或N：").upper()
#     if time != 'N':
#         print(time)

# 使用标志True或False，很多不同事件会导致程序停止运行，使用标志可以只判断某个条件时暂停循环，相当于初始化循环一直处于活跃状态
# active = True
# while active:
#     time = input("你要继续玩游戏吗？输入Y或N").upper()
#     if time == 'N':
#         active = False

# 使用break退出循环：要立即退出循环，不再运行循环余下代码可使用break
number = 1
while True:
    print("我爱学习")
    if number == 10:
        print("我已经说了十遍")
        break
    number += 1
print(number)

# 在循环中使用continue:返回循环的开头，并根据条件测试结果判断是否继续执行循环，不像break不执行后面代码并退出循环
n = 0
print("10以内的奇数有：")
while n < 10:
    n += 1
    if n % 2 == 0:
        continue
    print(n)

# 避免无限循环：每个while循环必须有停止运行的途径，这样才不会无限循环，为避免无限循环，务必对每个while循环进行测试
# i = 2
# while i < 4:
#     print(i)

# 练习：询问顾客年龄，并给出对应票价
# age = ''
# while True:
#     age = input("请输入你的年龄：")
#
#     if int(age) < 3:
#         print("免费")
#     elif int(age) <= 12:
#         print("￥10")
#     elif int(age) > 12:
#         print("￥15")
#     else:
#         print("输入错误，请重新输入")
#         break

# 使用while循环处理列表和字典
# 1.在列表之间移动元素
unconfirmed_users = ['ada','bob','joy']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"将用户{current_user.title()}添加到已验证用户表中")
    confirmed_users.append(current_user)
print("显示所有已验证的用户：")
for user in confirmed_users:
    print(user)

# 2.删除列表中特定元素
pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

# 3.使用用户输入来填充字典
responses = {}
# 设置一个标志，指出调查是否继续
polling_active = True
while polling_active:
    # 提示输入被调查者的名字和回答
    name = input("\nWhat is your name?")
    response = input("which mountain would you like to climb someday? ")
    # 将回答存储在字典中
    responses[name] = response
    # 看看是否有人要参与调查
    repeat = input("Would you like to let another person respond ? (yes/no)")
    if repeat == 'no':
             polling_active = False
    # 调查结束，显示效果
    print("\n---Poll Results ---")
    for name,response in responses.items():
            print(f"{name} would like to climp {response}.")