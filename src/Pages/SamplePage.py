import src.Modules.SampleModule as sm
from src.Scripts.BaseSpec import BaseClass
from selenium.webdriver.common.by import By
import properties

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







