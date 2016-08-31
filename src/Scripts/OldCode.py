
import pytest
import selenium
from selenium import webdriver
import Pages.properties as prop
from Pages.Base import BasePage
from Pages.SamplePage import FacebookPage


FBPage = FacebookPage()
base = BasePage()
# class TestSpec(unittest.TestCase):
#
#     @classmethod
#     def setUpClass(self):
#         if(prop.browser=="firefox"):
#             self.driver=webdriver.Firefox()
#         elif(prop.browser=="chrome"):
#             self.driver=webdriver.Chrome("C:\BrowserDriver\chromedriver_win32\chromedriver.exe")
#         base.setDriver(self.driver)
#         print('In Setup Class')
#         self.driver.maximize_window()
#         print (prop.websiteURL)
#         self.driver.get(prop.websiteURL)
#

def test_login(selenium):
        print("Hii")
        selenium.get(prop.websiteURL)
        selenium.maximize_window
        print (selenium.title)
        base.setDriver(selenium)
        print ("ENDING **********************")
        FBPage.login(selenium)
        #self.assertTrue("Log in to Facebook | Facebook", self.driver.title)
        print("Everything is completed")
#
# def test_login_2(selenium):
#         print("Hii")
#         selenium.get(prop.GmailwebsiteURL)
#         base.setDriver(selenium)
#         print("ENDING **********************")
#         FBPage.login(selenium)

# if __name__ == '__main__':
#     HTMLTestRunner.main()




