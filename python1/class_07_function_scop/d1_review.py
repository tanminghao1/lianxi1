"""
1,return 1.函数遇到return程序终止，后面紧跟着的值是函数返回值
2,参数的种类：1.位置参数，一一对应2.关键字参数，对换顺序3.默认参数：可以少传参
3,不定长参数，*args,不定长关键字参数：**kwargs

函数：1,作用 2,对于学习python非常重要，不需要每次百度
"""
# 查看函数源码来了解函数的作用
# import os
# os.execl()

# 函数的相互作用
# 函数的作用域
def main():
    # name,offer 定义在函数体里面还是函数体外面？
    name = '天天'
    offer = '40k'
    dalao(name,offer)
    pass

# def eat(dalaoname,food):
#     print('{}最喜欢吃{}'.format(dalaoname,food))
#     return

def dalao(name,money,food = '冰激凌'):
    print("恭喜{}拿到了一个{}的offer.".format(name,money))
    # eat(food)
    eat(name,food)
    # print('{}最喜欢吃{}'.format(name,food))
    return

def eat(dalaoname,food):
    print('{}最喜欢吃{}'.format(dalaoname,food))
    return
main()