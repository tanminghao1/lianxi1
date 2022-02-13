"""
1.收集测试用例:TestLoader,初始化一个加载器
2.查找测试用例,获取case_path，使用加载器查找testloader.discover(文件夹路径,'test_*.py(默认，不用传，根据文件名开头匹配)')
3.放到一个测试集合(测试套件) TestSuite = testloader.discover(case_path)
4.打开测试报告地址，初始化运行器runner=HTMLTestRunnerNew.HTMLTestRunner(),并运行测试结果将结果输出报告中runner.run(TestSuite)


# TestRunner,
1.会运行用例
2.生成测试报告
"""
import datetime
import time
import unittest
import os
from common import HTMLTestRunnerNew
from config.setting import config
# 1.初始化TestLoad加载器
testloader = unittest.TestLoader()
# 2.查找测试用例，加载,不再需要找到用例路径，直接写到config中，discover发现模块下所有用例，也可以通过模块名，类名查找用例
suite = testloader.discover(config.case_path)
# 3.测试报告
ts = str(int(time.time()))
file_name = f"test_result{ts}.html"
file_path = os.path.join(config.report_path,file_name)
# 如果报告是html格式，打开时需要以二进制方式打开"wb"，不需要encoding
with open(file_path,"wb") as f:
    # 初始化运行器，是以普通文本生成测试报告,verbosity报告形式，比较low一般不用
    runner = HTMLTestRunnerNew.HTMLTestRunner(f, title="前程贷接口测试报告", description=f"执行时间：")
    # 运行测试用例
    runner.run(suite)


