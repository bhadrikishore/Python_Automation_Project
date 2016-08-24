from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class BaseClass(object):

    driver=webdriver.Firefox()


    def getDriver(self):
        return self.driver

    def click(self,elementpath):

        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, elementpath)))
        element.click()


