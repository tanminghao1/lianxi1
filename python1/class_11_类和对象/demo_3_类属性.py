"""
类的属性：包括类属性和实例属性
类属性：类集体的属性

类属性：每一个成员都具备的特征
类里面表示的变量，就是属性
类属性又称为类变量

类属性获取：
1. 类名.属性名
2. 实例名.属性名
类属性的修改：
类名.属性名 = 新的属性值

实例属性，实例变量：
类成员自己独有的特征，并不是每个类成员都具备的
吉祥：喜欢重口味，男，名字，半夜写代码

如何去定义一个具体的对象：
具体的对象的定义，会在类的下面定义固定函数名称：__init__
    def __init__(self):
        pass
如何去使用对象，初始化一个对象出来，jixiang
初始化对象的时候：类名(参数1，参数2，参数3)
初始化对象的时候：__init__(self,参数1，参数2，参数3)
总结：具体对象使用的时候实际上是调用__init__
__init__函数返回值只能是None,不能是其他值，默认不写
TypeError: __init__() should return None, not 'str'


如何表示实例属性
实例属性定义：__init__里面：self.属性名= 属性值
实例属性的使用：实例名称(不是类名).属性名
实例属性的修改：实例名称.属性名= new属性值

self:是在类的定义当中，表示实例自己
"""
class BigBoss:
    # 类属性
    code_level = "very good"
    hair = "very thin"
    hobby = "宅"
    def __init__(self,name,food,gender):

        """定义具体的对象，初始化函数，初始化方法"""
        print(name)
        print(food)
        print(gender)
        # self只能在函数里面使用，外面用变量接收
        print("对象自己",self)
        # 定义实例属性
        self.dalao_name = name
        self.food = food
        self.gender = gender
        # 返回值只能是None，默认不写
        # return None
    # 定义一个普通函数
    def hello_word(self):
        """加了self，实例方法"""
        print(self.dalao_name,"wawawawa")
        return "哭出来是正常的"

# 获取类属性
print(BigBoss.code_level)
print(BigBoss.hair)
print(BigBoss.hobby)

BigBoss.hobby = "party"
print(BigBoss.hobby)

# 初始化对象，实例化对象，对象生出来
baby = BigBoss('jixiang','辣条','nan')
print("code)level",baby.code_level)

# 获取实例属性,实例名.参数
print(baby.gender)

# 类名的话就是所有对象都有的属性，错误
# print(BigBoss.gender)

print("外部对象自己",baby)
print(baby.hello_word())
""" 以下写法不可再调用，已简化成上面写法
# baby = BigBoss.__init__(BigBoss,'jixiang','辣条','nan')
# print(""code_level",baby.code_level)
"""