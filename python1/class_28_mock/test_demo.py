import unittest
from mock import Mock


def add(a,b):
    return a+b

class Testadd(unittest.TestCase):
    def test_add(self):
        add = Mock(return_value=8)
        self.assertEqual(7,add(3,4))