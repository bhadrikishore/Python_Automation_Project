import unittest

from selenium import webdriver
from src.Scripts.SamplePage import FacebookPage

#FBPage = FacebookPage()
class BaseSpec(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print('In Setup Class')
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def setUp(self):
        print('In Setup Method')

    def test_login(self):
        print("Hii")
        #FBPage.login()

    def tearDown(self):
        print('In TearDown Method')

    @classmethod
    def tearDownClass(self):
        print('In TearDown Class')

