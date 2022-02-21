# 在项目中创建测试用例的模块，以test开头文件，unittest默认

# 1.模块名以test开头 2.类 以Test开头 3.方法test开头
# 右击出现unittest，没有出现需要配置
import unittest
from class_16_requests.d3_unittest import visitor
url = 'http://test.lemonban.com/futureloan/mvc/api/member/login'
data = {"mobilephone":"18111111111","pwd":"123456"}
headers = {"name":"yuz"}
class TestLogin(unittest.TestCase):
    def test_login_success(self):
        # 测试代码丢进来
        # res = visitor(url,headers=headers,data=data)
        # print(res)
        # 加try except,抛出异常使程序执行下去
        try:
            self.assertEqual(1,2)
        except AssertionError as e:
            print("断言失败",e)
            # 断言失败后要抛出异常
            raise e

# 写完代码要空一行
# 如何运行：需要unitest.main()方法，右击出现unittest,如果未出现 手动添加
if __name__ == '__main__':
    unittest.main()

