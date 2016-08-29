import mypkg,unittest

class testcaseA(unittest.TestCase):

    def setUp(self):
        self.driver = mypkg.getOrCreateWebdriver()