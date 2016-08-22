from selenium import webdriver

class BaseClass(object):

    def browserLaunch(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("http://www.facebook.com")
        return self.driver

