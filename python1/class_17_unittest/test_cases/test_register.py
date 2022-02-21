import unittest

import requests


class TestRegister(unittest.TestCase):
    def test_register(self):
        self.assertEqual(1,1)

if __name__ == '__main__':
    unittest.main()

# url = 'http://test.lemonban.com/futureloan/mvc/api/member/login'
# header = {'name':'tan'}
# json = {"mobilephone":"18111111111","pwd":"123456"}
# class TestLogin(unittest.TestCase):
#     def test_login_success(self):
#         session = requests.sessions.session()
#         res = session.post(url=url,json=json,headers=header)
#         try:
#             self.assertEqual(1,res.json()["status"])
#         except AssertionError as e:
#             print("断言失败")
#             raise e


