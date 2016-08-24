from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from src.Scripts.BaseSpec import BaseClass

base = BaseClass()
class FacebookModule(BaseClass):

    driver = base.getDriver()

    def _init_(self):
        print('This is Sample Module Class')

    def getUsernameField(self):
        return self.driver.find_element(By.ID, "email")


    def getpassField(self):
         return self.driver.find_element(By.ID, "pass")




    #usernameField = driver.find_element(By.ID,"email")
    #passwordField = driver.find_element(By.ID,"pass")
    #loginButton = driver.find_element(By.ID,"u_0_l")
