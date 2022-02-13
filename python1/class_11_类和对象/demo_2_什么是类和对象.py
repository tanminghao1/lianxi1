"""
1.什么是类
具有相同的特征的某一些事物的种类，集合


小马哥是属于什么类？  人类，男人类，单身类
吉祥是属于什么类？    人类，女人类，非单身类，喜欢重口味

同样的一个人或物，可以属于多个类吗？可以属于多个类
不同的人和物，可以属于同一个类吗？ 可以

表示方法：

类的定义
class 类名():
    类的内容
    类体

类名表示：
- 类名也是标识符
- 字母，数字，下划线，且不能以数字开头
- 大驼峰命名：BigBoss  小驼峰：bigBoss

2.什么是对象
对象就是类当中的一个成员   TODO：如何表示某一个成员：吉祥

"""
# 类定义
class BigBoss:
    pass
# 类的使用，类的实例化，对象化，初始化
# 可以使用整个
# 使用整个
print(BigBoss)
# 使用类当中的一个成员 TODO：对象，实例
print(BigBoss())


# 1.创建Dog类
class Dog:
    """一次模拟小狗的简单尝试"""
    """__init__()方法在根据类创建新实例时，python会自动运行它"""
    def __init__(self,name,age):
        """初始化属性name和age"""
        """以self为前缀的变量可供类中的所有方法使用"""
        self.name = name
        self.age = age
    def sit(self):
        """模拟小狗收到命令时蹲下"""
        print(f"{self.name} is sitting")
    def roll_over(self):
        """模拟小狗收到命令时打滚"""
        print(f"{self.name} is rolled over")

# 2.根据类创建实例：可将类视为有关如何创建实例的说明。Dog类是一系列说明，让python知道如何创建表示特定小狗的实例
# 使用实参，调用类Dog创建一个表示特定小狗的实例，并使用提供的值来设置属性name和age，接下来python会返回一个小狗的实例，并将它赋值给my_dog。
my_dog =Dog('bob',1)
print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old")

# 3.访问属性：要访问实例的属性，可使用句点表示法.python先找到实例my_dog，再查找与实例相关联的属性，在Dog类中引用这个属性时，使用的是self.name
my_dog.age

# 4.调用方法：根据Dog类创建实例后，就能使用句点表示法来调用Dog类中定义的任何方法了
my_dog.sit()
my_dog.roll_over()

# 4.创建多个实例
my_dog = Dog('yellow',1)
your_dog = Dog('red',2)
print(f"My dog name is {my_dog.name}")
my_dog.sit()
print(f"Your dog name is {your_dog.name}")
your_dog.sit()

# 创建一个Restaurant的类，为其方法__init__()设置属性resturant_name和cuisine_type,创建一个名为describe_restaurant()的方法和一个名为
# open_restaurant()的方法，前者打印前述两项信息，后者打印一条信息餐馆正在营业
# 根据类创建实例restaurant的实例，分别打印其两个属性，再调用前述两个方法
class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"餐馆叫{self.restaurant_name}")
        print(f"餐馆经营{self.cuisine_type}")
    def restaurant_open(self):
        print(f"餐馆的营业时间是9:00-22:00")


my_resturant = Restaurant("望湘园","湘菜")
my_resturant.restaurant_open()
your_resturant = Restaurant("海底捞","火锅")
your_resturant.describe_restaurant()
he_resturant = Restaurant("城门口","火锅")
he_resturant.describe_restaurant()

# 创建一个User类，包含属性first_name,last_name,及其他属性，定义一个名为describe_user的方法打印用户信息摘要，再定义一个名为greet_user的
# 方法用于向用户发出问候语
class User:
    def __init__(self,first_name,last_name,age,sex):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
    def describe_user(self):
        print(f"{self.first_name}{self.last_name}的用户信息如下："
              f"\n年龄：{self.age}"
              f"\n性别：{self.sex}")
    def greet_user(self):
        print(f"你好呀，{self.first_name}{self.last_name}！")
user_jay = User("周","杰伦","37","男")
user_jay.describe_user()
user_jay.greet_user()
user_jj = User("林","俊杰","31","男")


# 2.使用类和实例：使用类模拟现实中很多情景，类编写后，大部分时间根据花在根据类创建的实例上，可以直接修改实例的属性，也可以编写方法以特定的方式进行修改
# 1>Car类
class Car:
    def __init__(self,make,model,year):
        """初始化藐视汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
    def get_descriptive_name(self):
        """返回整洁的描述信息"""
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()
my_newcar = Car("宝马","X3","2020")
print(my_newcar.get_descriptive_name())

# 给属性指定默认值
class Car:
    """初始化属性，新增里程:odometer属性，给属性指定默认值"""
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
    def get_descriptive_name(self):
        long_name = f"{self.make},{self.model},{self.year}"
        return long_name
    def read_odpmeter(self):
        print(f"这辆车开了{self.odometer}公里")
my_newcar = Car("宝马","X3","2020")
print(my_newcar.get_descriptive_name())
my_newcar.read_odpmeter()

# 修改属性的值
# 1>直接修改属性的值,访问属性并赋值
my_newcar.odometer = 23
my_newcar.read_odpmeter()

# 2>通过方法修改属性的值：无须直接访问属性，可将值传递给方法，由它在内部进行更新
class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odpmeter = 0
    def get_descriptive_name(self):
        long_name = f"{self.make},{self.model},{self.year}"
        return long_name
    def read_odpmeter(self):
        print(f"这辆车开了{self.odpmeter}公里")
    def update_odpmeter(self,mileage):
        self.odpmeter = mileage
my_newcar = Car("宝马","X3","2020")
my_newcar.update_odpmeter(50)
my_newcar.read_odpmeter()

# 对方法update_odpmeter()进行扩展，禁止任何人将里程表读数往回调
class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odpmeter = 0
    def get_descriptive_name(self):
        long_name = f"{self.make},{self.model},{self.year}"
        return long_name
    def read_odpmeter(self):
        print(f"这辆车开了{self.odpmeter}公里")
    def update_odpmeter(self,mileage):
        """将里程表设置为指定值，并禁止将里程表往回调"""
        if mileage >= self.odpmeter:
            self.odpmeter = mileage
        else:
            print("不能调低里程数")
    def increment_odometer(self,miles):
        """将里程表读数增加指定的值"""
        self.odpmeter += miles
my_newcar = Car("宝马","X3","2020")
my_newcar.update_odpmeter(10)
my_newcar.increment_odometer(100)
my_newcar.read_odpmeter()