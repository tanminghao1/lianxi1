"""
模块：.py文件
包：带有__init__.py文件的文件夹

1.模块名称：模块名称是否一个标识符
标识符命名规则：
1.数字、下划线、字母，不能以数字开头，不能关键字
2.模块名称命名一般是使用下划线的形式命名，驼峰
3.模块名称不能和python内置模块名称重合
random,内置模块。那么我们命名自己的模块的时候就不要使用random

包：python3，新版本不带__init__.py 同样可以作为包使用

2.模块导入
from 模块名称 import 类名，函数名，变量名     适用于项目根目录，或者内置模块
from (项目根目录下)包名.包名.包名.模块名 import 类名，函数名，变量名   自己定义的包名
from (项目根目录下)包名.包名.包名.模块名 import 模块名    导入整个模块
使用的时候，模块名.函数名

1.如果出现重名的函数，需要使用别名
2.函数名称很长，使用别名
公式 from 模块名称 import 类名，函数名，变量名  as rename

# import 只能是模块名 (as 别名)     适用内置模块
# 调用 模块名.函数名()
# import 包名.包名.模块名


3.查找模块的顺序，python只能发现根目录下开始查找

模块被导入的时候
from。。。import。。 会去读模块下所有顶格的代码
"""
from time import time
from random import randint
print(time())
print(randint(1,99))
# from 包名.包名.包名.模块名 import 类名，函数名，变量名
from class_09_import.module_1 import randint as ri
print(ri())


# import 只能是模块名 (as 别名)     适用内置模块
# 调用 模块名.函数名()
# import 包名.包名.模块名
import  time  # 模块名
time.time()
