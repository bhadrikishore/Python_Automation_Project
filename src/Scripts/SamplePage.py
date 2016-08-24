from selenium.webdriver.common.by import By

import properties
import SampleModule as sm
from BaseSpec import BaseClass

base = BaseClass()
class FacebookPage(object):

    driver = base.getDriver()

    def _init_(self):
        print("Reusable Functions")

    def login(self):
        print('In Login')
        base.type(By.ID, sm.userNameField, properties.userName)
        print ("After entering text into Username Field")
        base.type(By.ID, sm.passwordField, properties.password)
        base.click(By.ID,sm.loginButton)

    def loginFailure(self):
        print('In Login')
        base.type(By.ID, sm.userNameField, properties.userName)
        print ("After entering text into Username Field")
        base.type(By.ID, sm.passwordField, properties.password)
        base.click(By.ID,sm.loginButton)







