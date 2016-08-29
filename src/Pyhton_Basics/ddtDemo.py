import unittest
from ddt import ddt, data

@ddt
class MyTestClass(unittest.TestCase):
    @data(1, 2)
    def test_print(self, command):
        print command
