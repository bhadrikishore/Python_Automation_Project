from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

class BaseClass(object):

    driver = webdriver.Firefox()

    def getDriver(self):
        return self.driver


