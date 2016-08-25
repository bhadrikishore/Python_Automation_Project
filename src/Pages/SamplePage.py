from selenium.webdriver.common.by import By

import properties as prop
from src.Scripts.BaseSpec import BaseClass
from src.Modules import SampleModule as sm

base = BaseClass()
class FacebookPage(object):

    driver = base.getDriver()

    def _init_(self):
        print("Reusable Functions")

    def login(self):
        print('In Login')
        base.type(By.ID, sm.userNameField, prop.userName)
        print ("After entering text into Username Field")
        base.type(By.ID, sm.passwordField, prop.password)
        base.click(By.ID,sm.loginButton)

    def loginFailure(self):
        print('In Login')
        base.type(By.ID, sm.userNameField, prop.userName)
        print ("After entering text into Username Field")
        base.type(By.ID, sm.passwordField,prop.password)
        base.click(By.ID,sm.loginButton)







