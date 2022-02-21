import logging
import config

class Logger_fengzhuang(logging.Logger):
    def __init__(self,
                 name = 'root',
                 level = 'DEBUG',
                 file = None,
                 format = "%(asctime)s-%(filename)s-%(lineno)d-%(name)s-%(levelname)s-%(message)s"):
        super().__init__(name)
        self.setLevel(level)
        fm = logging.Formatter(format)
        if file:
            filehandler = logging.FileHandler(file)
            filehandler.setLevel(level)
            filehandler.setFormatter(fm)
            self.addHandler(filehandler)
        streamhandler = logging.StreamHandler()
        streamhandler.setLevel(level)
        streamhandler.setFormatter(fm)
        self.addHandler(streamhandler)


if __name__ == '__main__':
    logger = Logger_fengzhuang(config.LoggerConfig.logger_name, file=config.LoggerConfig.logger_file)
    logger.info("abc")