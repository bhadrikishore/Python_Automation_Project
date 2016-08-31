import pytest
import smtplib
from selenium import webdriver
import Pages.properties as prop
from Pages.Base import BasePage
from Pages.SamplePage import FacebookPage
FBPage = FacebookPage()
base = BasePage()

@pytest.fixture()
def cloneDriver(selenium):
    selenium.get(prop.websiteURL)
    selenium.maximize_window()
    # def driver_teardown():
    #         print ("Starting in driver tear down")
    #         selenium.find_element_by_id("userNavigationLabel").click()
    #         selenium.find_element_by_xpath("//*[@id='BLUE_BAR_ID_DO_NOT_USE']/div/div/div[1]/div/div/ul/li[12]").click()
    # request.addfinalizer(driver_teardown())
    # print ("Ending in driver tear down")
    return selenium

@pytest.mark.usefixtures()
def setupClass(self):
    print "set up class"

def test_login(driver):
    print("Hii")
    # driver.get(prop.websiteURL)
    # driver.maximize_window
    print (driver.title)
    base.setDriver(driver)
    print ("ENDING **********************")
    FBPage.login(driver)
    # self.assertTrue("Log in to Facebook | Facebook", self.driver.title)
    print("Everything is completed")

def test_google(driver):
    print "Google test"
    driver.get("http://www.google.com")

@pytest.mark.webtest
def test_gmail(cloneDriver):
    print "Gmail test"
    cloneDriver.get("http://www.gmail.com")

@pytest.mark.trylast
def setupClass_last(self):
    print "tear down class"


