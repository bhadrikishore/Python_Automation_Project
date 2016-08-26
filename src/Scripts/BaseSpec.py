from selenium import webdriver
import sys,properties as prop

from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class BaseClass(object):

    driver=webdriver.Firefox()

    def getDriver(self):
        return self.driver

    def click(self,locatorType,elementPath):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((locatorType, elementPath)))
        element.click()

    def type(self,locatorType,elementPath,value):
        if locatorType == By.ID:
            element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, elementPath)))
            element.send_keys(value)
        elif locatorType == By.Xpath:
            element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, elementPath)))
            element.send_keys(value)
        elif locatorType == By.css:
            element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, elementPath)))
            element.send_keys(value)
        else:
            print ("Please provide valid locator type")



