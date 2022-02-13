# OS模块
# 文件操作
# 异常处理

"""模块导入
模块如何导入
1.from 包.包.模块 import 函数名，类名，变量名
第一个包是项目名目录下开始的
2.from 包.包.模块 import 函数名，类名，变量名  as 别名
别名的作用：
1.避免和其他名称重复
2.名字太长时

3.from 包.包 import 模块名
3.5 from 包.模块 import *（通配符，所有的）

4.import 包.模块  （as 别名）
"""
# from class_10_file_handler.module_1 import run
# run()

# from class_10_file_handler import module_1
# module_1.run()

# *的用法
# 为什么不建议用*，导入非常混乱，容易造成名称冲突，强烈不建议使用
from class_10_file_handler.module_1 import *

# 调试定义好的函数或者类的使用
# 如果想直接执行某个python文件，那么就写一个if__name__
# main()
if __name__ == '__main()__':
    pass