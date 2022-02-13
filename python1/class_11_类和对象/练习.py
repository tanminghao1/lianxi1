# 创建一个骰子，默认6面，摇十次
from random import randint
class Die:

    def __init__(self,sides = 6):
        self.sides = sides
    @staticmethod
    def roll_die(self):
        for i in range(1,11):
            print(f"第{i}次摇骰子：{randint(1,self.sides)}")
tou_die = Die()
tou_die.roll_die()
# 创建一个10面的骰子
tou_die.sides = 10
tou_die.roll_die()
# 创建一个20面的骰子
tou_die.sides = 20
tou_die.roll_die()

# 调试定义好的函数或者类的使用
# 如果想直接执行某个python文件，那么就写一个if__name__
# main()
if __name__ == '__main()__':
    pass