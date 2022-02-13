from class_21_logger封装.logger_handler_2 import LoggerHandler

# 每次都要初始化一个logger，可以在logging直接初始化一个logger对象供项目内的其他模块使用
# 不用每次导入类，直接导入对象，一个项目一般就一个文件，大型项目可能不适用
from class_21_logger封装.logger_handler_2 import logger
# 不需要再初始化
# logger = LoggerHandler('python25',file='demo_log.txt')
def main():
    print("hello")
    logger.info('gg')
def hello():
    logger.error('hello')
def d1():
    logger.info('www')
if __name__ == '__main__':
    main()