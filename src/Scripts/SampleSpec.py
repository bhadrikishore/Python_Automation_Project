import unittest, time

from src.Pages.SamplePage import FacebookPage
from src.Scripts.BaseSpec import BaseClass


FBPage = FacebookPage()
base = BaseClass()
class TestSpec(unittest.TestCase):

    driver = base.getDriver()

    @classmethod
    def setUpClass(self):
        print('In Setup Class')
        self.driver.maximize_window()
        self.driver.get("http://www.facebook.com")

    def setUp(self):
        print('In Setup Method')

    def test_login(self):
        print("Hii")
        FBPage.login()

    def tearDown(self):
        print('In TearDown Method')

    @classmethod
    def tearDownClass(cls):
        print('In TearDown Class')

if __name__ == '__main__':
    unittest.main()

    # suite = unittest.TestSuite()
    # suite.addTest(unittest.makeSuite(TestSpec))
    # dateTimeStamp = time.strftime('%Y%m%d_%H_%M_%S')
    # buf = "TestReport" + "_" + dateTimeStamp + ".html", 'wb'
    # runner = HTMLTestRunner.HTMLTrepoestRunner(
    #         stream=buf,
    #         title='Test the Report',
    #         description='Result of tests'
    #         )
    # runner.run(suite)
# suite = unittest.TestLoader().loadTestsFromTestCase(TestSpec)
# unittest.TextTestRunner(verbosity=2).run(suite)



