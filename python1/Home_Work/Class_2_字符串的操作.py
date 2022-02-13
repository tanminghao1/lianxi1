# name = input("姓名:")
# age = input("年龄：")
# sexy = input("性别：")
#
# print("姓名："+name)
# print("年龄："+age)
# print("性别："+sexy)
# str1 = 'python cainiao 666'
# print(str1[4])
# # 切片复制
# str_two = str1[::]
# str_3 = str1[0:]
# print(str_two)
# print(str_3)
# # 找出字符串中间字符
# middle = int(len(str1) / 2)
# print(str1[middle - 1])
# print(str1[middle])
# # 切片
# print(str1[middle-1:middle+1])
# """卖橘子的计算器：
# 写一段代码提示用户输入的橘子价格和重量，
# 计算出应该支付的金额
# """
# pirce = input("价格：")
# weight = input("重量：")
# # input获取的数据类型都是字符串
# print(float(pirce) * float(weight))

"""
my_hobby = "Never Stop Learning"
"""
my_hobby = "Never Stop Learning"
# 2-6
print(my_hobby[1:6])
# 2-末尾
print(my_hobby[1:])
# 从开始到最后
print(my_hobby[:])
# 从开始到第6位
print(my_hobby[:6])
# 从索引3开始，每两个取一个
print(my_hobby[3::2])
# 从右边开始获取，倒数第2到倒数第5，步长为2
print(my_hobby[-2:-6:-2])
# 获取字符串末尾两个
print(my_hobby[-2:])
# TODO:字符串的逆序
print(my_hobby[::-1])
