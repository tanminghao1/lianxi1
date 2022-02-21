import os
import unittest

import requests


# class TestLogin(unittest.TestCase):
#     def setUp(self) -> None:
#         """前置条件
#         可以将初始化，数据放在前置条件当中
#         """
#         self.url = "http://test.lemonban.com/futureloan/mvc/api/member/login"
#         self.data = {"mobilephone":"18111111111","pwd":"123456"}
#         self.header = {"name":"tt"}
#         # 初始化一个session会话
#         self.session = requests.session()
#         print("前置条件")
#     def test_login_success(self):
#         res = self.session.post(url=self.url,headers=self.header,json=self.data)
#         self.assertEqual(0,res.json()['status'])
#
#     def tearDown(self) -> None:
#         print("后置条件")


# # 1.初始化用例执行加载器,用于收集测试用例
# from class_17_unittest.test_3_setUp import TestLogin
# from class_17_unittest.test_cases import test_login, test_register
#
# testloads =unittest.TestLoader()
# # 2.查找测试用例
# # 1>测试用例文件路径
# dirname = os.path.dirname(os.path.abspath(__file__))
# casepath = os.path.join(dirname,'test_cases')
# # 2>查找测试用例
# suit1 = testloads.discover(casepath)  #查找文件路径下所有匹配的用例  testloads.discover(case_path,'test_*.py')
# # suit2 = testloads.loadTestsFromTestCase(TestLogin)  # 查找指定的测试类
# # suit3 = testloads.loadTestsFromModule(test_login)  # 查找指定的模块
# # suit4 = testloads.loadTestsFromName() #
# # 初始化一个测试集suit，将用例添加到suit中
# total_suit = unittest.TestSuite()
# total_suit.addTest(suit1)
# # 初始化一个运行器
# run = unittest.TextTestRunner()
# # 运行测试集内的用例
# run.run(total_suit)


testloads = unittest.TestLoader()
dir_path = os.path.dirname(os.path.abspath(__file__))
case_path = os.path.join(dir_path,'test_cases')
suit1 = testloads.discover(case_path,'test*.py')
suit = unittest.TestSuite()
suit.addTest(suit1)
# 生成测试报告
report_path = os.path.join(dir_path,'report')
if not os.path.exists(report_path):
    os.mkdir(report_path)
file_path = os.path.join(report_path,'text_result.txt')
with open(file_path,mode='a',encoding='utf-8') as f :

    run = unittest.TextTestRunner(f,verbosity=2)
    run.run(suit)