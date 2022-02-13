"""
配置文件：便于管理项目当中的静态数据

配置：
变量，随时都会变化
常量，程序启动后，几乎不会发生变化

字典：
key:value   声音:80 网络：wifi
变量：
声音=80
网络=wifi

python的配置文件格式：
1.python模块，.py文件作为配置的文件
2.yaml文件 .yaml .yml

3. .ini文件  .conf文件  （以前用的多，现在用的少了）
结构：
片段：section
选项option,key字典
值：value
示例：
# 片段，下接选项，无法写注释
[teachers]
name = ['yuz','jianjian']
age = 16
gender = '男'
favor = ["movie":"追风","music":"周杰伦"]

[student]
name = ['谭','周']
age = 18

[excel]
file_name = 'data.xlxs'

[demo]
"""

# 1.封装logger模块，继承 小技巧：在定义的模块中初始化，在调用时保证是同一个logger
# 2.配置文件：python,yaml,ini(了解使用)
# python：直接通过模块下面的变量
# python:类，可以继承

# yaml
# 1.语法，key:value
# 2.读取，pyyaml  yaml.load(f.read(),Loader = FullLoader)


# ini
# 1.数据类型是str