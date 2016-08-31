from selenium.webdriver.common.by import By

import properties as prop
from Base import BasePage
base = BasePage()

userNameField = "email"
passwordField = "pass"
loginButton = "u_0_l"

GmailuserNameField = "Email"
GmailNextButton="next"
GmailpasswordField = "Passwd"
GmailSigninButton = "signIn"


class FacebookPage(object):


    def login(self,browser):
        print('In Login')
        base.type(By.ID, userNameField, prop.userName)
        print ("After entering text into Username Field")
        base.type(By.ID, passwordField, prop.password)
        base.click(By.ID, loginButton)

    def loginGmail(self,browser):
        print('In Login')
        print ("Entering username")
        base.type(By.ID, GmailuserNameField, prop.GmailuserName)
        print ("Clicking on  Next button")
        base.click(By.ID,GmailNextButton)
        print ("Entering password")
        base.type(By.ID, GmailpasswordField,prop.Gmailpassword)
        print ("Before last step")
        base.click(By.ID, GmailSigninButton)

