"""存储所有的配置项"""
# 第一种方法，直接设置变量
# logger_name = 'python25'
# logger_file = 'python25.txt'
import sys
# 第二种方法，写到class里，通过导入不同类来使用配置
class LoggerConfig:
    logger_name = 'python25'
    logger_file = 'python25.txt'
    level = 'DEBUG'
class ProductionConfig:
    level = 'WARNING'


# 通过环境使用什么样的配置项
# if sys.platform == 'linux':
#     config = ProductionConfig
# else:
#     config = LoggerConfig