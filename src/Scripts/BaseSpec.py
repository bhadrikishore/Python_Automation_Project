from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement



class BaseClass(object):

    def browserLaunch(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("http://www.facebook.com")
        return self.driver

    def clickElementByXpath(self,WebElement):
        print()

