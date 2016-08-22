import unittest
from src.Scripts.Test1 import abc
aObj = abc()
class xyz(unittest.TestCase):

    def test_meth(self):
        print("Hi")
        print(aObj.var)