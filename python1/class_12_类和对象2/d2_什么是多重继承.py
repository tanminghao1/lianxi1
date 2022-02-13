"""
子类可以继承多个父类，这些父类的所有属性方法子类都可以使用
"""


class MusicPlayer:
    def play(self):
        print("正在播放音乐")

class Game:
    def play(self):
        print("可以玩游戏")

class Phone:
    recharge = True
    def call(self):
        print("正在打电话")
    def send_msg(self):
        print("发送短信")

class SmartPhone(Phone,MusicPlayer,Game):
    def caputure_video(self):
        print("正在打视频")
    def call(self):
        self.caputure_video()
        print("正在打电话")
smatphone = SmartPhone()
smatphone.play()