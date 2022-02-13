# 格式化
# # print("姓名：")
# name = input("请输入姓名：")
# age = input("请输入年龄：")
# money = input("请输入年薪：")
# hobby = input("请输入兴趣：")
# # format方法使用
# # "my string {} other string {}".format(变量1，变量2)
# print("""*******
# 姓名：{}
# 年龄：{}
# 年薪：{}
# 兴趣：{}
# *******
# """.format(name,age,money,hobby))
# python 3.6及以上可使用f""进行字符串操作，类同于“{}”.format()
first_name = "stefen"
last_name = "cuRRy"
full_name = f"{first_name} {last_name}"
# .title() 将单词首字母格式化为大写单词
message = f"Hello,{full_name.title()}!"
print(message)
# 数据类型的转换
# age = '5'
# money = "4"
# # 转换成整型  int(str)
# print(int(age) * int(money))
# # 转化成字符串 str(int)
# ag = 5
# mon = 4
# print(str(age))