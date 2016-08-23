from src.Modules.SampleModule import FacebookModule
from src.Scripts.BaseSpec import BaseClass

FBModule = FacebookModule()
base = BaseClass()
class FacebookPage(object):

    def _init_(self):
        print("Reusable Functions")

    def login(self):
        print('In Login')
        FBModule.getUsernameField().send_keys("abc@gmail.com")



