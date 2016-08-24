from src.Modules.SampleModule import FacebookModule
from src.Scripts.BaseSpec import BaseClass
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import configparser


FBModule = FacebookModule()
base = BaseClass()
config = configparser.ConfigParser()
config.read('C:\Properties\properties.INI')
class FacebookPage(object):


    driver = base.getDriver()

    def _init_(self):
        print("Reusable Functions")

    def login(self):
        print('In Login')
        FBModule.getUsernameField().send_keys(config.get('LoginCredentials','username'))
        FBModule.getpassField().send_keys(config.get('LoginCredentials','password'))
        base.click()




