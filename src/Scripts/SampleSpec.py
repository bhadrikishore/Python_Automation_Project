import unittest,HTMLTestRunner

import Pages.properties as prop
from Pages.BasePage import BasePage
from Pages.SamplePage import FacebookPage

FBPage = FacebookPage()
base = BasePage()
class TestSpec(unittest.TestCase):

    driver = base.getDriver()

    @classmethod
    def setUpClass(self):
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
        #self.driver.quit()

    @classmethod
    def tearDownClass(self):
        print('In TearDown Class')

if __name__ == '__main__':
    HTMLTestRunner.main()




