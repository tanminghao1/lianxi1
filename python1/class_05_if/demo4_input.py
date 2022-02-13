# 函数input()：让程序暂停运行，等待用户输入一些文本，获取用户输入后，将其赋给一个变量
# message = input("用户输入名字\n将其打印出来：")
# print(message)

# 使用int()来获取数值输入
# 使用input()时，python将用户输入解读为字符串
# age = input("你多大了：")
# print(f'input()默认解读为字符串形式：{type(age)}')
# age = int(age)
# print(f"使用int()函数后的年龄为数值：{type(age)}")

#
# height = input("请输入你的身高：")
# height = int(height)
# if height >= 150:
#     print("\t超过免票身高")
# else:
#     print("\t免票")

# TODO：求模运算符：“%”，取余
# 判断一个数是奇数还是偶数
numbers = [3,2,4,65,8]
for number in numbers:
    if number % 2 == 0:
        print(f"{number}是偶数")
    else:
        print(f"{number}是奇数")