# 在项目中创建测试用例的模块，以test开头文件，unittest默认

# 1.模块名以test开头 2.类 以Test开头 3.方法test开头
# 右击出现unittest，没有出现需要配置
# 运行2，如何使用python去运行
import unittest
# from class_17_unittest.d3_unittest import visitor
# url = 'http://test.lemonban.com/futureloan/mvc/api/member/login'
# data = {"mobilephone":"18111111111","pwd":"123456"}
# headers = {"name":"yuz"}
class TestLogin(unittest.TestCase):
    def test_login_2_success(self):
        # 测试代码丢进来
        # res = visitor(url,headers=headers,data=data)
        # print(res)
        # 加try except,抛出异常使程序执行下去
        print("用例1")
        try:
            self.assertEqual(1,3-2)

        except AssertionError as e:
            print("断言失败",e)
            # 因为异常被捕获了，即使断言失败也不会抛出异常
            # 如果你想断言失败，要抛出异常，通过raise
            raise AssertionError
    def test_login_3_erro(self):
        print("用例2")
        self.assertEqual(1,2)


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