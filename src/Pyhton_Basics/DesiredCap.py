import unittest
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def setUp(self):
        self.driver = driver = webdriver.Remote(command_executor='http://172.16.30.201:4444/wd/hub', \
                                            desired_capabilities={ \
                                                "browserName": "firefox", \
                                                "version": "35", \
                                                })

        self.driver.implicitly_wait(30)
        self.base_url = "http://www.google.com"
        self.verificationErrors = []
        self.accept_next_alert = True
        driver.get("http://www.google.com")