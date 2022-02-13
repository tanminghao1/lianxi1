class Phone:
    def __init__(self):
        self.age = 10
    recharge = True
    def call(self):
        print("正在打电话")

class SmartPhone(Phone):
    def __init__(self):
        super().__init__()
    def call(self):
        self.caputure_video()
        # print("智能手机正在打电话")
        # 调用父类方法，又初始化了一个新的对象，会造成问题
        # Phone.call()
        # 使用supper()方法就是调用父类的方法，而不是自己的
        super().call()
    def caputure_video(self):
        print("正在视频")
smart = SmartPhone()
smart.call()
print(smart.age)