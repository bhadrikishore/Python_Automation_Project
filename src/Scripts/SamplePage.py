from selenium import webdriver
from src.Scripts.SampleModule import FacebookModule

FBModule = FacebookModule()
class FacebookPage(object):

    def _init_(self):
        print("Reusable Functions")

    def login(self):
        print('In Login')
        FBModule.driver.maximize_window()
        FBModule.driver.get("http://www.facebook.com")
        #uname_field = WebDriverWwait(driver,10).until


