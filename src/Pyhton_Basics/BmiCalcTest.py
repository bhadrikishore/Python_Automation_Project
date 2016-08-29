import unittest
from selenium.webdriver.firefox.webdriver import WebDriver as FirefoxDriver
from selenium.webdriver.chrome.webdriver import WebDriver
from BmiCalcPage import BmiCalcPage
import properties


class BmiCalcTest(unittest.TestCase):
      def test_calc(self):
        print ("**************STARTING*******************")
        driver = WebDriver()
        bmi_calc = BmiCalcPage(driver)
        bmi_calc.open()
        self.assertEqual(True, bmi_calc.is_loaded)
        bmi_calc.calculate('181','80')
        self.assertEqual('24.4', bmi_calc.bmi)
        self.assertEqual('Normal', bmi_calc.bmi_category)
        print ("**************ENDING*******************")
        #driver.close()
if __name__ == '__main__':
    unittest.main()