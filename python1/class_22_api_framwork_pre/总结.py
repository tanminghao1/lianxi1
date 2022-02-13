"""
1.py文件村塾的数据，变量，类
2.yaml,通用的 1.冒号后面要空格 2.缩进用空格键
3.ini文件，传统的使用频率高，现在用yaml较多

为什么测试完接口还需要进行UI测试
-接口注重的是服务端测试，并不能测前端显示

为什么测了UI还要进行接口：
-界面上没有问题：虽然说都是显示同一个答案，登录成功，服务器内部不知道实现逻辑是否符合“2*2=2+2”
-UI有问题，定位问题，定位BUG
"""

import yaml
with open("D:\pythonProject\python1\class_21_logger封装\python25.yaml",encoding="utf-8") as f:
    data = yaml.load(f,Loader=yaml.FullLoader)

from configparser import ConfigParser
# 初始化
config = ConfigParser()
# 读取文件
config.read('python25.ini',encoding='utf-8')
a = config.get('teachers','name')
print(a)
print(type(a))



