"""
__file__  :模块的路径
__name__  :表示运行python文件的模块名
如果当前模块是用来作为程序运行的脚步文件（入口文件），
__main__:表示运行python文件的模块名

如果不是程序运行的脚本文件，是作为模块导入其他的地方的
包名.模块名
"""
from class_09_import import module_1
print(__file__)
# print("主程序",__name__)
# print(module_1.randint())
# if __name__ == '__main__':
#     print("hello word")

# 当.py文件被作为脚本或者入口执行的时候，if下面的代码会执行
# 如果.py文件被导入其他模块调用时，if下面的代码不会被执行