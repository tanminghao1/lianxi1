# 编写类时，并非总是从空白处开始。如果要编写的类是另一个现成类的特殊版本，可使用继承。
# 一个类继承另外一个类时将自动获得另外一个类的所有属性和方法
# 原有的类称为父类，而新的类称为子类，子类继承父类所有属性和方法，同时还可以定义自己的属性和方法

# 1.子类的方法__init__()
# 在既有类的基础上编写新类时，通常要调用父类的方法__init__()，这将初始化在父类__init__方法中定义的所有属性，从而让子类包含这些属性

#创建一个电动汽车类，它具备Car类的所有功能
class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odpmeter = 0
        self.fill = 80
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
    def fill_gas_tank(self):
        print(f"该车的油箱为{self.fill}升")
# 创建子类，继承父类Car
class ElectricCar(Car):
    """电动汽车的独特之处。"""
    """定义__init__()方法"""
    def __init__(self,make,model,year):
        """初始化父类的属性"""
        """让python调用父类Car中定义的方法__init__()"""
        super().__init__(make,model,year)

my_tesla = ElectricCar("特斯拉","Moder Y","2021")
print((my_tesla.get_descriptive_name()))

# 创建子类时，父类必须包含在当前文件中。且位于子类前面，定义子类时，必须在圆括号内指定父类的名称。
# 方法__init__()接受创建Car实例的所需的信息
# supper()是一个特殊函数，让你能够调用父类的方法，这行代码让Python调用Car类的方法__init__(),让Electriccar实例包含这个方法中定义的所有属性
# 父类也称为超类(superclass),名称super由此而来

# 2.给子类定义属性和方法
class ElectricCar(Car):
    """
    初始化父类的属性
    再初始化子类的特有属性
    """
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery_size = 75
    def describe_battery(self):
        print(f"这辆车的电池容量是：{self.battery_size}度电")
my_tesla = ElectricCar("特斯拉","mdel Y","2021")
print(my_tesla.describe_battery())

# 3.重写父类的方法：可在子类中定义一个与父类方法同名的方法，这样python将不会考虑这个父类的方法，而只关注你在子类中定义的相应方法
# 对于父类的方法，只要它不符合子类模拟的实物的行为，都可以进行重写
# 假设父类Car有一个名为fill_gas_tank()的方法,它对电动汽车毫无意义，重写该方法
class ElectricCar(Car):
    """
    初始化父类的属性
    再初始化子类的特有属性
    """
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery_size = 75
    def describe_battery(self):
        print(f"这辆车的电池容量是：{self.battery_size}度电")
    def fill_gas_tank(self):
        print("电动汽车没有油箱")
my_tesla = ElectricCar("特斯拉","model Y","2021")
print(my_tesla.fill_gas_tank())

# 4.将实例用作属性:属性和方法清单越来越长时，可以将类的一部分提取出来
class Battery:
    """一次模拟电动汽车电瓶的简单尝试"""
    def __init__(self,battery_size = 75):
        self.battery_size = battery_size
    def describe_battery(self):
        print(f"这辆车的电池容量是{self.battery_size}度")
    def get_range(self):
        """打印一条消息，指出续航里程"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"这辆车的续航里程是：{range}公里")

class ElectricCar1(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery()
my_tesla1 = ElectricCar1("特斯拉","model Y","2021")
my_tesla1.battery.describe_battery()
my_tesla1.battery.get_range()


# 多重继承
"""
class 子类名(父类1，父类2，父类3)
    pass
"""
# 如果所有的父类都有同一个方法，根据代码当中继承的父类的先后顺序查找方法
# 类的定义：所有类都是继承object
# 类名:    类名()  类名(object)