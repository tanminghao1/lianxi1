# 在项目中创建测试用例的模块，以test开头文件，unittest默认

# 1.模块名以test开头 2.类 以Test开头 3.方法test开头
# 右击出现unittest，没有出现需要配置
# 运行2，如何使用python去运行

"""
ddt思想:数据驱动的思想：data,driven,testing
作用：灵活的管理测试数据，让每一组测试数据是一个独立的测试用例，不用写重复的测试类
你会data driven testing数据驱动思想

现在所说的是一个叫做ddt的python库
ddt库是和unittest搭配起来使用的，是unittest的一个插件
python/unittest/ddt自动化测试框架
使用方法：
@ddt.ddt    类上方没有括号
class TestDemo:
    @ddt.data()    方法上方有括号
    def test_demo(self):
        pass
"""
import unittest
import warnings
# 改用自己重新封装的ddt，放到自己的libs
from class_19_excel.libs import ddt
# import ddt
import json
from class_19_excel.comon.excel_handler import ExcelHandler
from class_19_excel.comon.request_handler import RequestHandler
# 调用封装的excel方法读取数据
test_data = ExcelHandler(r"C:\Users\86176\Desktop\cases.xlsx").read('Sheet1')
# 读取到的excel数据都是str类型,可以用json.loads对读取到的‘{"":""}’数据转化为{"":""}格式
# aa =json.loads(test_data[0]["headers"])
# 也可用eval()将字符串转化为字典
# print(type(eval(test_data[0]["data"])))
# test_data =[ {"url":"http://test.lemonban.com/futureloan/mvc/api/member/login",
#               "method":"post",
#               "headers":{"name":"yuz"},
#               "data":{"mobilephone":"18111111111","pwd":"123456"},
#               "expected":"hello word"},
#
#              {"url":"http://test.lemonban.com/futureloan/mvc/api/member/login",
#               "method":"post",
#               "headers":{"name":"yuz"},
#               "data":{"mobilephone":"181111","pwd":"123"},
#               "expected":"hello word"
#              }
#              ]
@ddt.ddt
class TestLogin(unittest.TestCase):
    def setUp(self) -> None:
        warnings.simplefilter('ignore', ResourceWarning)
    def tearDown(self) -> None:
        print("用例执行完毕")
    # 参数前加*，传不定长参数
    @ddt.data(*test_data)
    # 将*test_data当中的一组测试数据赋值到data这个参数中
    # 这样就不需要通过循环的方式传递参数或者写多个测试用例来执行
    def test_login(self,data):
        # 测试代码丢进来
        res = RequestHandler().visit(data["url"],
                                     data["method"],
                                     json=eval(data["data"]),
                                     headers=eval(data["headers"]))
        print(res)
        # self.assertEqual(res['msg'],data['excepted'])
        print("测试用例通过")

# 执行unitest时加一个if __name__ == '__main__'，表示使用python运行时才执行，使用unittest时不会被执行
if __name__ == '__main__':
    unittest.main()
# 使用unittest运行unitest.main()时会被运行两次，导致不会执行用例，要加if main()
# print("正在运行python")
# unittest.main()
# 如果两者混合用不会执行案例
# 断言结果：
"""
1. "."表示断言通过
2.F False表示断言没有通过
3.E Erro表示程序内部错误

用例执行顺序：
1.根据ascii编码排序
2.如果我们想手工调整测试用例的执行顺序，在不同的字母前加数字
pycharm运行的注意事项：
1.在空行处右击，执行整个模块
2.在类名上执行，执行单个测试类
3.在方法名上执行，执行当个测试用例
tips:注意在指定位置运行，空行的地方去运行

通过命令行运行：
python -m unittest class_17_unittest\test_login.py
python -m unittest class_17_unittest\test_login.py test_login.TestLogin
python -m unittest class_17_unittest\test_login.py test_login.TestLogin.test_login_2_success
"""