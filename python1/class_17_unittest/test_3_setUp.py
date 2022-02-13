"""
setUp:每次测试用例方法执行之前都会执行的方法，前置条件
可以把测试数据放单setUp中

tearDown:每次用例方法执行后的都会执行的方法，后置条件
过程：先执行setUp,然后执行test_...测试用例方法，最后执行tearDown
"""
import unittest
from class_17_unittest.d3_unittest import visitor
# url = 'http://test.lemonban.com/futureloan/mvc/api/member/login'
# data = {"mobilephone":"18111111111","pwd":"123456"}
# headers = {"name":"yuz"}
# excepted = {"name":"yuz"}

# data = {"url":"http://test.lemonban.com/futureloan/mvc/api/member/login",
#         "headers":{"name":"yuz"},
#         "data":{"mobilephone":"18111111111","pwd":"123456"},
#         "excepted":"hello world"
#         }
class TestLogin(unittest.TestCase):
    # 把数据放到前置条件当中
    # 每一个测试用例方法执行之前都会运行的代码
    # ->None只是语法表示，可以去掉
    def setUp(self) -> None:
        print("正在准备测试数据")
        self.data = {"url":"http://test.lemonban.com/futureloan/mvc/api/member/login",
        "headers":{"name":"yuz"},
        "data":{"mobilephone":"18111111111","pwd":"123456"},
        "excepted":"hello world"
        }
    def tearDown(self) -> None:
        print("用例执行完毕")
    def test_login_1_success(self):
        print("用例1")
        res = visitor(self.data['url'],self.data['data'],self.data['headers'])
        self.assertEqual(self.data['excepted'],res)

    def test_login_2_erro(self):
        print("用例2")
        self.assertEqual(1,1)

if __name__ == '__main__':
    unittest.main()


