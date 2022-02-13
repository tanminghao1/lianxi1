'''
1.os
查找现在文件的绝对路径
绝对路径：每次都要从最开始的地方查找D:\pythonProject\python1\class_11_类和对象\demo_1_总结.py
相对路径：根据现有的路径进行查找,D:\pythonProject\python1
demo_1_总结.py相对于D:\pythonProject\python1 为class_11_类和对象\demo_1_总结

# demo_1_总结.py 相对于 demo文件夹 ..
. 表示当前层级目录
..表示上级目录

2.文件读写
f = open(file_path,mode= 'r',encoding='utf-8')
f.read() #读取文件，根据光标读取内容   手动控制光标seek()
f.readlines() # 读取返回列表形式

既想读取又想写入，open(file_path,'w+',encoding=utf-8)
3.异常处理

try:
    执行
except Exception as e:   #Exception 通用，具体：TypeError,NameError
    print(e)
'''
# 现在的项目名称python1
# 根据现在的文件路径获取项目根目录路径
# import os
# dir_name = os.path.dirname(os.path.abspath(__file__))
# print(dir_name)
# # 找到dir_name的文件夹
# root_path = os.path.dirname(dir_name)
# print(root_path)
# # 判断文件是否存在，如果存在就创建
# if not os.path.exists(dir_name):
#     os.mkdir(dir_name)
#
#
# file_path = os.path.join(dir_name,'xiaofeng.txt')
# f = open(file_path,'w+',encoding='utf-8')
# f.write('xiaofeng is boss')
# # w模式下不能读取
# # 使用‘w+’可以写入后读取，因为光标在最后，读取的是空
# # 先关闭文件再读取
# # f.close()
# # 或使用seek()移动光标
# f.seek(0)
# print('读取',f.read())
#
# f.close()


try:
    print(['1'][100])
    print({"name":"yuz"}["bala"])
except (IndexError,KeyError):    #出现一种就可以捕获
    print("hello")
    # 下面抛出一个异常，我要告诉程序报一个错误，终止程序
    raise NameError
# except KeyError:
#     print("key")
finally:
    # 无论有没有报错，程序是否正常执行，都会执行的语句
    print("本本很生气")


def add(a,b):
    if not isinstance(a,int):
        raise ValueError
    return a+b
print(add(1,2))

# 文件操作，不管文件有没有正常打开，我都执行
import os
dir_name = os.path.dirname(os.path.abspath(__file__))
print(dir_name)
root_path = os.path.dirname(dir_name)

try:
    file_path = os.path.join(dir_name,'xiaofeng.txt')
    f = open(file_path,'w+',encoding='utf-8')
    f.write('xiaofeng is boss')
except Exception as e:
    print(e)
finally:
    f.close()

# with f = open()  自带finally:f.close
with open(file_path,'w+',encoding='utf-8') as f:
    f.write('langlang')
