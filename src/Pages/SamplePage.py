import src.Modules.SampleModule as sm
from src.Scripts.BaseSpec import BaseClass
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import configparser
import properties


base = BaseClass()
config = configparser.ConfigParser()
config.read('C:\Bhadri\Automation_Projects\Python_Automation_Project\properties.INI')
class FacebookPage(object):


    driver = base.getDriver()

    def _init_(self):
        print("Reusable Functions")

    def login(self):
        print('In Login')
        base.type(By.ID, sm.userNameField, properties.userName)
        base.type(By.ID, sm.passwordField, properties.password)
        base.click(By.ID,sm.loginButton)





