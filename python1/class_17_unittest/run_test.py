"""
1.收集测试用例:TestLoader,加载器
2.放到一个测试集合(测试套件) TestSuite

# TestRunner,
1.会运行用例
2.生成测试报告
"""
import unittest
import os
# 1.初始化TestLoad
from class_17_unittest import test_assert
from class_17_unittest.test_cases import test_login
from class_17_unittest.test_cases.test_login import TestLogin
from class_17_unittest.test_cases.test_register import TestRegister

testloader = unittest.TestLoader()
# 2.查找测试用例，加载
dir_path = os.path.dirname(os.path.abspath(__file__))
case_path = os.path.join(dir_path,'test_cases')
# testloader.discover(文件夹路径,'test_*.py(默认，不用传，根据文件名开头匹配)')发现测试用例
# 将你想运行的用例，放到指定文件夹中
# suite = testloader.discover(case_path)
# 运行指定模块的用例
# suite = testloader.loadTestsFromModule(test_assert)
# 运行多个模块的用例
# suite2 = testloader.loadTestsFromModule(test_login)
# 将两个suite添加到同一个套件里
# suite_total = unittest.TestSuite()
# suite_total.addTests(suite)
# suite_total.addTests(suite2)
# suite = testloader.loadTestsFromName()

# 添加指定的测试类
suite = testloader.loadTestsFromTestCase(TestLogin)
suite2 = testloader.loadTestsFromTestCase(TestRegister)

suite_total = unittest.TestSuite()
suite_total.addTests(suite)
suite_total.addTests(suite2)
print(suite_total)

# report
report_path = os.path.join(dir_path,'report')
if not os.path.exists(report_path):
    os.mkdir(report_path)
file_path = os.path.join(report_path,'test_result.txt')
# text
with open(file_path,"w",encoding='utf-8') as f:
    # 初始化运行器，是以普通文本生成测试报告,verbosity报告形式，比较low一般不用
    runner = unittest.TextTestRunner(f,verbosity=2)
    # 运行测试用例
    runner.run(suite_total)

# 几种加载测试用例的方法：
# 1.用的最多的，整个项目一起加载，使用discover
# 2.你想只测试某一个具体的模块，功能，使用 loadTestFromTestCase 或者loadTestFromModule
# 3.pytest