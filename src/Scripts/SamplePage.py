from selenium import webdriver

from src.Scripts.SampleModule import FacebookModule

FBModule = FacebookModule(webdriver)
class FacebookPage(object):

    def _init_(self):
        print("Reusable Functions")

    def login(self):
        FBModule.driver.maximize_window()
        FBModule.driver.get("http://www.facebook.com")
        #uname_field = WebDriverWwait(driver,10).until


