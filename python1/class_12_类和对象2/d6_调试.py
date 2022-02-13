"""debug
调试：
1.最简单的方式print(),出现问题先print(a),调试完了要删除
2.出现问题先print()，再百度
3.打断点，优先使用的调试

如何使用debug模式：
1.小虫子的标记，断点配合起来用
2.断点：程序运行到红点的地方，会暂停
3.调试工具：
step over f8:下一行，单步调试
resume program下一个断点
run to cursor运行到指定行
step into 进入到函数方法对应的代码,step out退出对应函数代码

"""
# 既能打电话又能录音
class Phone:
    def __init__(self,model,color):
        self.model = model
        self.color = color
    def call(self,record = True):
        if record == True:
            self.record()
        print("正在打电话")
    def record(self):
        print(f"{self}正在进行录音")
    """repr返回对象打印出来的效果，名字固定用法"""
    def __repr__(self):
        """"""
        return self.model
phone = Phone("iphone12","red")
phone.call(False)
phone.record()
# class SmartPhone(Phone):
#     a = 4
#
#     def call(self):
#             self.caputure_video()
#     def caputure_video(self):
#         print("正在视频")
#
# smart = SmartPhone()
# smart.call()