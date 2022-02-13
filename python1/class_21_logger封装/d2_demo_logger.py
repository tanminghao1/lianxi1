from class_21_logger封装.d1_demo_logger import d1
from class_21_logger封装.logger_handler_2 import LoggerHandler
# 模块里直接导入logger对象使用
from class_21_logger封装.logger_handler_2 import logger


# 同一个包下的日志文件要是一样才能确保不同模块的日志生成在同一个文件
# logger = LoggerHandler('python26',file='demo_log.txt')
def main():
    logger.info('aaa')
    # 调用其他模块方法时也会执行logger，会导致生成多个logger，所以要统一日志文件
    # 可以在配置文件配好logger,避免写错文件名
    # 或者调用同一个对象，在logging模块里初始化一个logger进行导入
    d1()
def hello():
    logger.error('word')
if __name__ == '__main__':
    main()