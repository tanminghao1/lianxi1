# 导入config标准库
from configparser import ConfigParser
# 初始化
config = ConfigParser()
# 读取文件
config.read('python25.ini',encoding='utf-8')
a = config.get('teachers','name')
print(a)
# 拿到的是字符串
print(type(a))


