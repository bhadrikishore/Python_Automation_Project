from selenium import webdriver
from selenium.webdriver.common.by import By
from src.Scripts.BaseSpec import BaseClass

base = BaseClass()
class FacebookModule(BaseClass):

    driver = base.browserLaunch()

    def _init_(self):
        print('This is Sample Module Class')

    def getUsernameField(self):
        usernameField = self.driver.find_element(By.ID, "email")
        return usernameField

    #usernameField = driver.find_element(By.ID,"email")
    #passwordField = driver.find_element(By.ID,"pass")
    #loginButton = driver.find_element(By.ID,"u_0_l")
