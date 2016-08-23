import unittest
from selenium import webdriver
from src.Pages.SamplePage import FacebookPage
from src.Scripts.BaseSpec import BaseClass

FBPage = FacebookPage()
base = BaseClass()
class TestSpec(unittest.TestCase):

    driver = base.getDriver()

    @classmethod
    def setUpClass(self):
        print('In Setup Class')
        self.driver.maximize_window()
        self.driver.get("http://www.facebook.com")

    def setUp(self):
        print('In Setup Method')

    def test_login(self):
        print("Hii")
        FBPage.login()

    def tearDown(self):
        print('In TearDown Method')

    @classmethod
    def tearDownClass(cls):
        print('In TearDown Class')

suite = unittest.TestLoader().loadTestsFromTestCase(TestSpec)
unittest.TextTestRunner(verbosity=2).run(suite)

