"""
方法，类里面的函数就叫方法
方法和属性的关系
属性：特征、名词
方法：行为、动作、动词
方法和方法之间的相互调用
带有self参数的方法叫做实例方法
self可以修改

没有self的方法
1.静态方法
就是表示刚刚好放在类下面的普通函数
只是为了方便管理我们的代码
静态方法的调用  self.方法  类.方法

类方法：
cls代表类本身
类方法的调用：类.方法名    实例.方法名
"""
def eat(food):
    return "大佬喜欢吃{}".format(food)

class Dalao:
    favor = 'python'
    def __init__(self,name):
        self.name = name

    @staticmethod
    def eat(food):
        print("大佬喜欢")
        return "大佬喜欢吃{}".format(food)
    def offer(self,money,food):
        print("恭喜{}拿到{}的offer".format(self.name,money))
        food = self.eat(food)
    @classmethod
    def code(cls):
        print("我喜欢的编程语言是{}".format(cls.favor))
dalao = Dalao("克拉美学")
# dalao.offer("40k","辣条")
# dalao.eat("辣条")
Dalao.code()
dalao.code()

"""
类的继承
1.功能机，智能机
phone的所有属性和方法，smartphone都可以使用
phone是smartphone的父类
如何继承：class 类名(父类名)
重写：如果父类和子类有相同的方法和属性，优先使用子类的方法和属性
"""
class Phone:
    recharge = True
    def call(self):
        print("正在打电话")
    def send_msg(self):
        print("发送短信")
class SmartPhone(Phone):
    def caputure_video(self):
        print("正在打视频")
    def call(self):
        self.caputure_video()
        print("正在打电话")
smartphone = SmartPhone()
smartphone.call()
print(smartphone.recharge)