import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from src.Pages.SamplePage import FacebookPage
from src.Pyhton_Basics import Basics

FBPage = FacebookPage()
class BaseSpec(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        inh = Basics()
        print("Hii.. " + inh.var)
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def setUp(self):
        driver = self.driver
        driver.get("http://www.python.org")
        assert "Python" in driver.title
        elem = driver.find_element_by_name("q")
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

    def test_login(self):
        driver = self.driver
        driver.get("http://www.google.com")

    def tearDown(self):
        driver=self.driver

    @classmethod
    def tearDownClass(self):
        self.driver.close()
        self.driver.quit()

