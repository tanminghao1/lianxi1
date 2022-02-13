# 不定长参数
# 我不知道需要定义多少个参数
def sum(a,b):
    total = 0
    return total + a + b
# print(sum(2,3))

def sum_total(a,b,*args,name = 'yuz',**kwargs):
    """
    *args 表示剩下多余的参数
    **kwargs 表示剩下多余的关键字参数
    """
    # 在函数定义里面，可以用*args去接收多余位置参数
    # 在函数的定义里面，args是元组
    # 函数体里kwargs 是字典的形式，接收多余的关键字参数
    print(args)
    print(kwargs)
    total = 0
    c = total + a + b
    for i in args:
        c += i
    return c
# print(sum_total(3,4,5,1,2,1))


# 可以是列表也可以是元组，脱掉括号都一样
rest = [1,2,3]
# rest = (1,2,3)
# 因为集合是无序的，会导致位置参数变化
# rest = {1,2,3}
# 在函数的调用中，也可以用*value去传其他剩余的参数
# print(sum_total(3,4,*rest))
# print(sum_total(3,4,1,2,3))

# 函数外面可以通过**values传其他关键字参数
other_info = {'hobby':'girl','food':'辣条'}
# 转化为hobby = 'girl',food = '辣条'
sum_total(1,2,3,4,name = 'feiqu',age = 18,**other_info)
# sum_total(1,2,3,4,name = 'feiqu',age = 18,hobby = 'girl',food = '辣条')

# 总结
# 函数的返回值return，return后面是返回值，return语句之后不生效，遇到return就终止
# 函数的参数，位置参数：一一对应
# 关键字参数：1.好记，有标记 2.可以换顺序
# 默认参数：可以少传参数
# 注意：顺序，位置参数最前面，关键字参数和默认参数是在后面
# 不定长参数，动态参数。1.不定长位置参数：*args,*C,*b函数体里叫不定长位置参数和函数外叫参数解包
# 2.关键字不定长参数：**kwargs,**a,**b

# 1.传递任意数量的实参：不知道要传递多少个实参，可以使用*形参来接收，是一个元组（），通用形参名：*args,也可自定义
def make_pizza(*toppings):
    print(toppings)
make_pizza("葱花","香菜")
make_pizza("花椒")

def make_pizza(*toppings):
    print("顾客的披萨需要放：")
    for topping in toppings:
        print(topping)
make_pizza("葱花","香菜","胡椒粉")
make_pizza("葱")

# 2.结合使用位置参数和任意数量的实参：位置参数作为必传参数，其他参数为非必传参数，放在最后，python先匹配位置参数和关键字参数，再将剩余参数收到最后形参中
def make_pizza(size,*args):
    print(f"顾客需要一个{size}寸的披萨，并需要添加：")
    for arg in args:
        print(arg)
make_pizza('5','葱花','香菜')

# 3.使用任意数量的关键字参数**kwargs：预先不知道传递给函数是什么样的信息，可以接收任意关键字参数
# 例：函数接收姓和名，还接收其他用户信息
def user_info(firstname, lastname,  **userinfo):
    """多余的关键字参数以键值对传入，形成一个字典，定义一个空的字典接收多余的关键字参数"""
    userinfo['firstname'] = firstname
    userinfo['lastname'] = lastname
    return userinfo
user1 = user_info("谭","铭昊",shengao = "170",tizhong = "140")
print(user1)