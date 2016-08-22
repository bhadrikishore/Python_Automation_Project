from selenium import webdriver

class BaseSpec:

    def setUp(self,BrowserName):
        self.BrowserName=BrowserName
        if(self.BrowserName=="Firefox"):
            self.driver = webdriver.Firefox()
        elif(self.BrowserName=="Chrome"):
            self.driver=webdriver.Chrome("C:\BrowserDriver\chromedriver_win32\chromedriver.exe")
        elif(self.BrowserName=="Chrome"):
            self.driver=webdriver.Chrome("C:\BrowserDriver\IEDriverServer_x64_2.53.1\IEDriverServer.exe")
        else:
            print "Please specify Browser correctly"

    def Test_URL_Invoke(self,URL):
        self.driver.get(URL)

    def tearDown(self):
        self.driver.close()




