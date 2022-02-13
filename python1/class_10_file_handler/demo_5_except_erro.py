"""
异常：程序无法按照预计结果走，一旦出现错误，程序无终止行

try:
    我要执行的可能出现错误的代码
    当没有错误，那么try就会执行完
    一旦出现错误，立即跳到except里面
except（Exception）:           #默认捕获所有异常类型（语法错误除外）
    出现异常以后要运行的代码
except 异常类型:   #捕获特定错误类型
"""

"""
num1 = input("请输入数字1")
num2 = input("请输入数字2")
try:
    print("hello")
    print(num1*num2)
    print("word")
except:
    # 异常的捕获catch,如果出现错误，按照我说的做
    print("这里有个BUG")
    try:
        1 / 0
    except:
        print("except又有bug")
    print("finish")
print("trycash异常处理")
"""
# 为什么不直接使用默认的捕获
# 1.不方便定位问题
# 2.不确定是什么原因造成异常
# 3.一般不是使用默认的，而是会加入异常类型


num1 = 'a'
num2 = 'b'
try:
    print("hello")
    print(num1 * num2)
    print("word")
# 期望捕获“IndexError”
# except IndexError:
except Exception as e:   #通过别名打印错误信息
    print("这里有个BUG",e)



# 常见错误类型
# ImportError:无法导入模块或包
# IndexError:下标索引超出序列边界
# NameError:使用一个还未赋予对象的变量,没有定义
# SyntaxError:代码逻辑语法出错，不能执行，不能去捕获
# TypeError:传入的对象类型与要求不符
# ValueError:传入一个不被期望的值，即使类型正确
# KeyError:试图访问你字典里不存在的键
# IOError:输入输出异常，文件操作

# NameError
# print(abc)

# IndexError
# print(['a','b'][100])

# KeyError
# print({"a":"yuz"}["xianren"])

# 总结
"""
os模块，记住用法，os.path.abspath, oa.path.dirname()
os.mkdir  创建文件夹
os.path.exists()  是否存在

open(filename,'w',encoding='utf-8')
f.close()
f.read()
f.readlines()
f.wirte()

异常处理：
try:
    ..
except 类型 as  e:
    ...
print("其他的代码")
"""