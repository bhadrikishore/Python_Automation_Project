from src.Modules.SampleModule import FacebookModule
from src.Scripts.BaseSpec import BaseClass

FBModule = FacebookModule()
base = BaseClass()
class FacebookPage(object):

    def _init_(self):
        print("Reusable Functions")

    def login(self):
        print('In Login')
        #FBModule.driver.maximize_window()
        #FBModule.driver.get("http://www.facebook.com")
        FBModule.getUsernameField().send_keys("abc@gmail.com")
        base.clickElementByXpath(FBModule.getUsernameField())



