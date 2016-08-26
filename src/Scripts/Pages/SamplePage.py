from selenium.webdriver.common.by import By

import Python_Automation_Project.properties as prop
from BasePage import BasePage
from Python_Automation_Project.src.Modules import SampleModule as sm

base = BasePage()
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


