class A:
    def play(self):
        print("a is playing")
class B(A):
    def play(self):
        print("b is playing")
class C:
    def play(self):
        print("c is playing")
class D(B,C):
    # def play(self):
    #     print("d is playing")
    pass
d = D()
d.play()
# 当继承方法有相同方法时，调用顺序
# 广度优先：继承的父类们继承了同一个父类时，使用广度优先，先找C的方法
# 深度优先：继承的父类们未继承同一个父类时，使用深度优先，先找B的父类方法
# 当前用C3算法：当继承形成菱形时使用广度，未形成菱形时使用深度

# 当有继承更多个父类时，不清楚是否形成菱形问题,使用.mro方法查看查找顺序
# 查找方法的顺序
print(D.__mro__)