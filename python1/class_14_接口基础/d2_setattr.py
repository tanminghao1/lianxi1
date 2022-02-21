"""
setattr()设置属性，动态获取某个属性的值
setattr(对象或者类名,‘属性名称’,‘不管属性存在是否有值，都赋新值’)
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

phone = Phone("apple")
phone.brand = "小米"
print(phone.brand)

# 获取属性，如果不存在就会报错
# 修改,类似字典
phone.color = "red"
print(phone.color)

setattr(phone,"food","辣条")
print(phone.food)

setattr(phone,"brand","oppo")

# 有时候我们提前不知道属性名称是什么，是从别的地方拿过来的
#