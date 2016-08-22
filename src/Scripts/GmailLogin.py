import unittest
from BaseSpec import BaseSpec
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class GoogleLogin(unittest.TestCase):

    def setUp(self):
         s=BaseSpec()
         s.setUp("Chrome")
         print "Browser invoked"

    def test_google_login1(self):
        print "before navigating to URL"


        # elem = s.find_element_by_id("Email").send_keys("bhadrikishore02@gmail.com")
        # s.find_element_by_id("next").click()
        # s.implicitly_wait(20)
        # pwd=s.find_element_by_xpath("//*[@id='Passwd']").send_keys("rajamma*")
        # s.find_element_by_id("signIn").click()
        # print s.title
        # assert "No results found." not in driver.page_source

    def tearDown(self):
        print "Browser is going to close"
        b = BaseSpec()
        b.tearDown()

#First way of running the scripts(Useful while running the scripts through Commmand line)
if __name__ == '__main__':
   unittest.main()

#Second way of running the scripts
# suite = unittest.TestLoader().loadTestsFromTestCase(GoogleLogin)
# unittest.TextTestRunner(verbosity=1).run(suite)

#Third way of running the scripts with script name

