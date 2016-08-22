import unittest

from src.Pages.SamplePage import FacebookPage

FBPage = FacebookPage()
class BaseSpec(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('In Setup Class')

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

if __name__ == "_main_":
    unittest.main()

