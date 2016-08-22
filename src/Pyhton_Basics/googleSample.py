
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Firefox()
driver.maximize_window()
driver.get("http://www.python.org")
elem=driver.find_element_by_name("q")
elem.send_keys("python")
elem.send_keys(Keys.ENTER)
        
