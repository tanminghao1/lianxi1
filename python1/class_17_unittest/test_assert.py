"""
断言方式：
assertTrue,判断条件
assertEqual,判断a,b是否相等
assertGreater,a>b
assertIn,a in b
assertRegex(),正则表达式匹配
"""
import unittest
class TestLogin(unittest.TestCase):
    def test_login_2_success(self):
        #
        expected = 2
        actual = 2
        # 断言方法，assertEqual会打印具体的预期结果和实际结果
        self.assertEqual(expected,actual)
        # assertTrue不会打印具体预期结果和实际结果
        # self.assertTrue(expected == actual)
        # assertGreater，比较预期结果和实际结果大小
        # self.assertGreater(expected,actual)
if __name__ == '__main__':
    unittest.main()
