"""
1.日志收集器 logger:日记本
2.日志收集器级别 level
3.日志处理器准备 handler 不同记号的笔
4.日志处理器级别设置
5.logger.addHandler(handler)
6.设置日志格式 format  日期：重要程度：分类（工作，生活） 内容
7.添加日志处理器

设置级别
当设成debug的时候，只有高于，等于该级别的才会打印
当你设成warning，只有warning，error,critical才会打印
"""

import logging
# 1.初始化logger收集器
logger = logging.getLogger("python25")

# 2.设置收集器级别，默认是warning,其他级别要设置，不然低于warning的不会打印
logger.setLevel("DEBUG")
# 笔的默认级别是warning,默认是使用控制台输出,不需要写
# handler = logging.StreamHandler()

# 3.初始化日志处理器，放到一个file文件当中,初始化笔，怎么输出日志
# 路径默认在当前文件夹下，可写绝对路径  logging.FileHandler("log.txt")  文件-日志处理器
handler = logging.FileHandler("log.txt")
handler.setLevel("DEBUG")

# 4.设置不同日志处理器来收集不同级别日志,logging.StreamHandler() 控制台-日志处理器
console_handler = logging.StreamHandler()
console_handler.setLevel("DEBUG")



# 5.收集器和处理器绑定起来，添加handler
logger.addHandler(handler)
logger.addHandler(console_handler)

# 6.设置handler格式,固定设置,官方文档查看
# %(filename)s 模块名字
# %(lineno)d 行号
# %(asctime)s 时间
#
fmt = logging.Formatter('%(asctime)s-%(filename)s-%(lineno)d-%(name)s-%(levelname)s-%(message)s')
# 7.将格式添加到handler
handler.setFormatter(fmt)
console_handler.setFormatter(fmt)


logger.info("hello")
logger.warning("word")
logger.debug("debb")