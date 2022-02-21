

# 1.初始化用例收集器
import os
import time
import unittest

from class_18_report import HTMLTestRunnerNew
from class_18_report.test_cases import test_login
from class_18_report.test_cases.test_register import TestRegister

test_load = unittest.TestLoader()
# 通过文件路径，查找测试用例
dir_path = os.path.dirname(os.path.abspath(__file__))
case_path = os.path.join(dir_path,"test_cases")
suit1 = test_load.loadTestsFromModule(test_login)
suit2 = test_load.loadTestsFromTestCase(TestRegister)
# 初始化测试套件
total_suit = unittest.TestSuite()
total_suit.addTest(suit1)
total_suit.addTest(suit2)

# 测试报告地址和文件
report_path = os.path.join(dir_path,"report")
if not os.path.exists(report_path):
    os.mkdir(report_path)
ts = str(int(time.time()))
file = os.path.join(report_path,f"{ts}.html")
with open(file,"wb") as f:
    run = HTMLTestRunnerNew.HTMLTestRunner(f,verbosity=2)
    run.run(total_suit)
