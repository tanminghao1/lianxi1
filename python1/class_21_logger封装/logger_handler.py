import logging
# 不太高级，可以直接继承logging
class LoggerHandler():
    def __init__(self,
                 name='root',
                 level='DEBUG',
                 file=None,
                 format='%(filename)s-%(lineno)d-%(name)s-%(levelname)s-%(message)s'):
        # 初始化日志收集器
        logger = logging.getLogger(name)
        # 设置日志收集器级别
        logger.setLevel(level)
        fmt = logging.Formatter(format)
        # 初始化日志处理器,如果有创建两个，如果没有默认创建
        if  file:
            # 如果传了file,初始化handler
            file_handler = logging.FileHandler(file)
            # 设置handler级别
            file_handler.setLevel(level)
            # 设置format日志格式
            file_handler.setFormatter(fmt)
            # 处理器添加到收集器
            logger.addHandler(file_handler)
        # 默认初始化一个StreamHandler
        stream_handler = logging.StreamHandler()
        # 设置StreamHandler级别
        stream_handler.setLevel(level)
        # 设置format日志格式
        stream_handler.setFormatter(fmt)
        # 处理器添加到收集器中
        logger.addHandler(stream_handler)
        self.logger = logger
    def debug(self,msg):
        return self.logger.debug(msg)
    def info(self,msg):
        return self.logger.info(msg)
    def warning(self,msg):
        return self.logger.warning(msg)
    def error(self,msg):
        return self.logger.error(msg)
    def critical(self,msg):
        return self.logger.critical(msg)

if __name__ == '__main__':
    logger = LoggerHandler()
    logger.debug("hello")
