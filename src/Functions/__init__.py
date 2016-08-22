from selenium import webdriver

class SampleSpec:
    global driver
    def bhadri1(self, name, age):
            driver = webdriver.Firefox()
            self.name = name
            self.age = age
            #    driver=webdriver.firefox();
            print "my name is {0} and my age is {1}".format(self.name, self.age)