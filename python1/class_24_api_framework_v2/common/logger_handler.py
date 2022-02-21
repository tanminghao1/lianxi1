import logging
from common import yaml_handler
from config.setting import config

class LoggerHandler(logging.Logger):
    def __init__(self,
                 name='root',
                 level='DEBUG',
                 file=None,
                 format='%(filename)s-%(lineno)d-%(name)s-%(levelname)s-%(message)s'):
        # 初始化日志收集器，getlogger(name)已经进行了实例化
        # logger = logging.getLogger(name)
        # 直接继承父类的logger实例，返回的实例就是self了
        super().__init__(name)
        # 设置日志收集器级别
        self.setLevel(level)
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
            self.addHandler(file_handler)
        # 默认初始化一个StreamHandler
        stream_handler = logging.StreamHandler()
        # 设置StreamHandler级别
        stream_handler.setLevel(level)
        # 设置format日志格式
        stream_handler.setFormatter(fmt)
        # 处理器添加到收集器中
        self.addHandler(stream_handler)
        # self.logger = logger
yaml_data= yaml_handler.yaml_read(config.yaml_config_path)
# 初始化一个logger供其他模块调用
logger = LoggerHandler(yaml_data["logger"]["name"],file=config.log_file)

# if __name__ == '__main__':
#     logger = LoggerHandler()
#     logger.debug("hello word")