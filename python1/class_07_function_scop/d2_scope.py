# def main():
#     # name,offer 定义在函数体里面还是函数体外面？
#     # name = '天天'
#     # offer = '40k'
#     print(name,offer)
# name = 'kk'
# offer = '20k'
# print(name)
# main()
#
# print(name)

# 函数体内定义的变量叫局部变量，局部变量只能在函数体里生效
# 函数体外定义的变量叫全局变量，可以在函数体里使用
# name = '闲人'
# def dalao():
#     name = 'andy'
#     print("{}is dalao".format(name))
# dalao()
# print(name)
# id() 查看某个值或者变量在内存中的地址
# 函数的参数是局部变量

# 全局变量和局部变量的修改
# 局部变量能在函数体当中被修改吗
# 全局变量能在局部变量中能被修改吗
name = '晓峰'
def dalaos():
    # 函数体内修改局部变量
    # 此name非全局变量name
    # ocal variable 'name' referenced before assignment
    # 未被定义就引用
    global name
    name = name +'jajj'
    # 获取全局变量，如果要修改全局变量，需要先声明 global
    # 在函数体里可对全局变量进行修改

    print("{} is dalao".format(name))
    return name
# 函数体外不能获取局部变量
# global全局变量声明，但是现阶段不建议使用global，容易造成数据混乱
print(dalaos())
print(name)

# 内置函数，python内部放置的函数，不需要我们去定义的函数
# print() input() len() type() min() setattr() slice() id()
# sorted() enumerate() eval() sum() rund() zip()
# range()是一个类
# .join() .format()不是内置函数
# print(min(1,2,3))
# for index,i in enumerate([1,7,9,6]):
#     # 获取索引
#     print(index,i)
# eval()脱字符串的衣服，对字符串解包
# print("1+5")
# print(eval("1+5"))
# 四舍五入
# print(round(3.33))