from selenium import webdriver

class BaseSpec:

    def __init__(self):
        self.driver = webdriver.firefox()
        self.driver.get("http://www.google.com")
        print "Started"






