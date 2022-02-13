"""
log 日志
日志：记录
代码当中：日志的作用是记录信息，便于我们查看问题，定位问题
logging:标准库
日志级别：
1.NOSET     0  等于没写
2.debug     10 调试，一些额外信息，备注，往往和主体功能无关
3.info      20 主体功能的信息，日报，做了些啥
4.warning   30 警告，下次可能要出错
5.error     40 报错
6.critical  50崩溃
"""

import logging

def old_function():
    try:
        1 / 0
        logging.info("代码没有问题")
    except Exception as e:
        # logging是写入错误
        logging.error(e)
        # raise是抛出异常，后续代码不会运行
        raise e
    logging.warning("这个方法下个版本不会再用，请用新的方法")
    return "hello"
def new_function():
    return "new_function"
a = 1
b = 2
c = a + b
# 记录debug信息
logging.info("这是一个普通的信息")
logging.debug("这是一个debug信息")

logging.warning("这是一个警告信息")
logging.error("出错了，兄嘚")
logging.critical("崩溃了")


if __name__ == '__main__':
    old_function()