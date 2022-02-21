"""如果想使用别人已经写好的模块或者包

如果不是python内置的：
1.放到目录下面，作为一个包或者模块
2.External Libararies--lib/site-packages    --外部库

os模块是别人写好的，python内置的
主要用来处理系统相关的

os.path 用来处理系统路径相关的

"""

import os.path
# pwd 显示当前文件的工作路径，相对路径
# 你在哪里运行的python指令，这个路径就是当前文件路径
# 每次会变，取决于你在哪里运行的python,相对路径
# print(os.getcwd())

# 如果想每次得到的一样，要用绝对路径:abspath()/realpath()
print(os.path.abspath(__file__))

# 获取路径下文件夹名称：dirname
print(os.path.dirname(__file__))
a = os.path.dirname(os.path.abspath(__file__))
# 路径拼接，组成一个完整路径：os.path.join()
print(os.path.join(a,'yuze.txt'))

# os.mkdir(路径名字)：在某个目录下创建一个新目录
# 先得到data目录的绝对路径
# 创建文件一次建一级
data_path = os.path.join(a,'data')
# os.mkdir(data_path)
# 是否是一个文件夹
print(os.path.isdir(data_path))
print(os.path.isdir(a))

# 是否是一个文件
print(os.path.isfile(a))

# 路径是否真的存在
print(os.path.exists(data_path))
xianren_path = os.path.join(a,'xianren')
print(os.path.exists(xianren_path))
print(xianren_path)
# 判断data是否存在，如果存在，pass,如果不存在，创建一个
if not os.path.exists(xianren_path):
    os.mkdir(xianren_path)
