"""
1.实现一个手机类，并实例化你的手机
要求类里要有属性+行为，至少应该具有品牌，型号等信息，拨打电话，发短信等功能
尽量多的获取不同属性和使用不同的功能
"""

class Mobile():
    # 类属性
    if_capture = '能拍照'

    def __init__(self,brand,module,color):
        self.brand = brand
        self.module = module
        self.color = color
    def call(self,phone_num):
        return "我正在打电话"
    def send_msg(self):
        return "发短信"


mobile = Mobile("xiaomi","6","黑色")
print(mobile)

"""
2.灰色的Tom猫，今年1岁，吃着美味的食物，喝着可口的饮料，非常享受的样子
a.根据以上信息抽象出一个类
b.定义相关属性，并能在类的外面调用
c.定义相关方法，在方法中打印相应信息
object ==》对象
总结：
1.如果不清楚到底是类属性还是实例属性，那么先给它做成实例属性

"""
class cat:
    def __init__(self,name,age,color):
        self.name = name
        self.age = age
        self.color = color
    def eat(self,food_name = '美味的'):
        print("一只叫{}的猫，正在吃美味的食物",format(self.name))
    def drink(self,drink_name = '可乐'):
        print(f"一只叫{self.name}的猫，正在喝饮料")

tom = cat('tom','1','灰色')
print(tom.name)

"""
3.编写如下程序：
a.创建一个名为Restaurant的类，要求拥有饭店名(restaurant_name)和美食种类(cooking_type)两个属性
b.需要创建一个名为describe_restaurant()的方法(描述饭店名和美食种类相关信息)和一个名为open_restaurant()的方法
c.根据这个类创建一个名为restaurant的实例，分别打印其两个属性，再调用前述两个方法
"""
class Restaurant(object):
    def __init__(self,name,cooking_type):
        self.restaurant_name = name
        self.cooking_type = cooking_type
    def describe_restaurant(self):
        # 类里面去获取实例的属性 self.属性名称
        print("本饭店叫{self.restaurant_name},拥有的美食种类有{self.cooking_type}".format(self.restaurant_name,self.cooking_type))
    def open_restaurant(self):
        print(f"{self.restaurant_name}正在营业")

res = Restaurant('饭店名',['红烧肉','茄子煲','辣椒炒肉'])
print(res.cooking_type)