from selenium import webdriver
from selenium.webdriver.common.by import By

class FacebookModule(object):

    driver = webdriver

    def _init_(self,driver=webdriver):
        print('This is Sample Module Class')


    #usernameField = driver.find_element(By.ID,"email")
    #passwordField = driver.find_element(By.ID,"pass")
    #loginButton = driver.find_element(By.ID,"u_0_l")
