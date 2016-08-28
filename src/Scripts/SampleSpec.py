import unittest,HTMLTestRunner
from selenium import webdriver
import Pages.properties as prop
from Pages.Base import BasePage
from Pages.SamplePage import FacebookPage
import Pages.properties

FBPage = FacebookPage()
base = BasePage()
class TestSpec(unittest.TestCase):

    @classmethod
    def setUpClass(self):

        if(prop.browser=="firefox"):
            self.driver=webdriver.Firefox()
        elif(prop.browser=="chrome"):
            self.driver=webdriver.Chrome("/usr/local/bin/chromedriver")

        base.setDriver(self.driver)
        print('In Setup Class')
        self.driver.maximize_window()
        print (prop.websiteURL)
        self.driver.get(prop.websiteURL)

    def setUp(self):
        print('In Setup Method')

    def test_login(self):
        print("Hii")
        FBPage.login()
        self.assertTrue("Log in to Facebook | Facebook", self.driver.title)
        print("Everything is completed")

    def tearDown(self):
        print('In TearDown Method')
        self.driver.quit()

    @classmethod
    def tearDownClass(self):
        print('In TearDown Class')

if __name__ == '__main__':
    HTMLTestRunner.main()




