from selenium.webdriver.common.by import By

import properties as prop
from BasePage import BasePage
base = BasePage()

userNameField = "email"
passwordField = "pass"
loginButton = "u_0_l"

class FacebookPage(object):

    driver = base.getDriver()

    def _init_(self):
        print("Reusable Functions")

    def login(self):
        print('In Login')
        base.type(By.ID, userNameField, prop.userName)
        print ("After entering text into Username Field")
        base.type(By.ID, passwordField, prop.password)
        base.click(By.ID, loginButton)

    def loginFailure(self):
        print('In Login')
        base.type(By.ID, userNameField, prop.userName)
        print ("After entering text into Username Field")
        base.type(By.ID, passwordField,prop.password)
        base.click(By.ID, loginButton)


