
"""
getattr()动态获取某个属性的函数，内置函数
getattr(对象或者类名,‘属性名称’,‘当没有此属性时，提供的默认值’)
"""
class Phone:
    # 类属性
    recharge = True
    def __init__(self,brand):
        # 实例属性
        self.brand = brand
    def call(self):
        self.xianren = '男'
        print("正在打电话")
    def send_msg(self):
        print("正在发短信")
iphone = Phone("apple")
print(iphone.brand)
# 如果获取没有存在的属性，会报错
# print(iphone.color)
# iphone.call()
# 在方法中定义属性，需先调用方法才能调用属性，
# print(iphone.xianren)
# # 属性brand已存在，不会取‘小米’
# print(getattr(iphone,'brand','小米'))
# # 属性xianren不存在，设置默认值‘大佬’
# print(getattr(iphone,'xianren','大佬'))

# 类名.类属性    类名.实例属性是错误的
print(getattr(Phone,'brand','xiaomi'))
print((getattr(Phone,'recharge','False')))

phone2 = Phone("oppo")
print(phone2.brand)