"""
1.编写如下程序，尝试函数的部分封装：
a.用户输入1-7个数字，分别代表周一到周日
b.如果输入1-5，打印对应的’周一‘~’周五‘，输入6,7打印'周末'
c.如果输入0，退出循环
d.输入其他内容，提示“输入有误，请重新输入”
提示：本题可使用if，while循环，同时需判断用户输入是否正确，不用考虑浮点数等情况
"""


# 写函数时先写注释，把主流程思路写下来，再去不断封装函数
def main():
    """主流程"""
    pass  # 占位符


main()


def get_week_name_1(num):
    """
    最简单的方法
    :param num:
    :return:
    """
    if num == '1':
        print("今天周一")
    elif num == '2':
        print("今天周二")
    elif num == '3':
        print("今天周二")
    pass


def get_week_name(num):
    """
    根据num的值得到周几
    :param num:
    :return:
    """
    dict_week = {'1': '周一', '2': '周二', '3': '周三', '4': '周四', '5': '周五', '6': '周末', '7': '周末'}
    if num == 0:
        return 'break'
    elif num not in dict_week.keys():
        return ('error')
    else:
        # dict_week['1']
        return (dict_week[num])


def if_num(out):
    while True:
        if out == 'break':
            break
        elif out == 'error':
            print("输入信息有误")
        elif out == '周末':
            print("周末")
        else:
            print(out)
        break


def main_1(num):
    # while True:
    #     num = input("请输入1-7中一个数字：")
    # 根据num的值判断今天是周几，get_week_name(num)
    out = get_week_name(num)
    return if_num(out)
    # if_num(out)
    # if out == 'break':
    #     break
    # elif out == 'error':
    #     print("输入信息有误")
    #     break
    # else:
    #     print(out)
    #     break


# num = input("请输入1-7中一个数字：")
# main_1(num)

"""
2.列表去重
将列表[10,1,2,20,10,3,2,1,15,20,44,56,3,2,1]去除重复元素
"""


# set去重,set集合不存在相同元素且无序
def deduple_1(my_list):
    # my_list = [10,1,2,20,10,3,2,1,15,20,44,56,3,2,1]
    return list(set(my_list))


# 其他方法,一个个取出来存到新的列表中，如果存在就不添加
def deduple(my_list):
    new_lis = []
    for item in my_list:
        if item not in new_lis:
            new_lis.append(item)
    return (print("去除重复元素字后列表new_lis为：{}".format(new_lis)))


my_list = [10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]
# deduple(my_list)
# print(deduple_1(my_list))

"""
3.将两个变量的值进行交换：a = 200,b = 100
"""


def swap(a, b):
    return b, a


def swap2(a, b):
    temp = a
    a = b
    b = temp
    return a, b


# print(swap(1,3))
# print(swap2(1,3))

"""
4.编写如下程序，尝试函数部分封装：
输入一个人的身高(m)和体重(kg)，根据BMI公式(体重除以身高的平方)计算BMI值
a.例如:一个65公斤的人，身高是1.62m，则BMI为：65 / 1.62 **2 = 24.8
b.根据BMI值给与相应的提醒
低于18.5：过轻，18.5-25：正常，25-28：过重，28-32：肥胖，高于32：严重肥胖
"""


def get_bmi(height, weight):
    """
    计算bmi
    :param height:
    :param weight:
    :return:
    """
    return weight / height ** 2


def get_warning(bmi):
    if not bmi:
        return ("输入数据有误")
    elif bmi < 18.5:
        return ("过轻")
    elif 18.5 <= bmi < 25:
        return ("正常")
    elif 25 <= bmi < 28:
        return ("过重")
    elif 28 <= bmi < 32:
        return ("肥胖")
    else:
        return ("严重肥胖")


def main_4(height, weight):
    # height = float(input("请输入身高："))
    # weight = float(input("请输入体重："))
    # 根据输入的参数计算BIM值，需要写注释就可以想办法写成函数
    # 1.可读性强 2.可以复用 3.代码更简洁
    # calc_bmi(height,weight)
    bmi = get_bmi(height, weight)
    # 根据bmi的值输出提示
    return (get_warning(bmi))


# height = float(input("请输入身高："))
# weight = float(input("请输入体重："))
# print(main(height,weight))

"""函数

def func_name(params1,params2):  #形式参数
    # 函数体
    # 函数体里的内容在外部无法查看
    return values  #输出函数的结果
"""


def dalao(name):
    new_name = 'DALAO' + name
    return new_name
    # print("吴梦是真大佬")    # 函数体中程序遇到return终止，后面代码不会再执行


# 函数定义好后需要调用才能执行里面的逻辑
# new = dalao("吴梦")
# print(new)

# return 注意
def get_bmi2(height):
    if height > 185:
        return '高富帅'
    # 省略了else：pase
    # else:
    #     pass
    print('不是高富帅')
    if height < 34:
        return '矮穷矬'
    # 省略了else：pase
    # else:
    #     pass
    print('也不是矮穷矬')
    return '普通人'


get_bmi2(190)
get_bmi2(173)
# print(get_bmi2(180))
