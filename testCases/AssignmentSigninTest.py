import unittest
from selenium import webdriver
import sys
sys.path.append("C://Users/Vanajakshi/PycharmProjects/PythonUnitTestProject_POMBased")
from pageObjects.AssignmentSigninPageObject import Signin


class SigninTest(unittest.TestCase):
    txturl = "http://automationpractice.com/index.php"
    txtbrowser = "chrome"
    txtvalidsigninemail = "kodavativanajakshi1@gmail.com"
    txtinvalidsigninemail = "aaaaaaaaaaaa"
    txtvalidsigninpwd = "1234567"
    txtinvalidsigninpwd = "aaaaaa "
    txtemptysigninemail= " "
    txtemptysigninpwd= "  "
    driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.txturl)
        cls.driver.maximize_window()


############################# POSITIVE TESTING ################################

    def test_valid_signin(self):
        si=Signin(self.driver)
        si.open_website(self.txturl)
        si.click_signinbtn()
        si.enter_valid_email(self.txtvalidsigninemail)
        si.enter_valid_pwd(self.txtvalidsigninpwd)
        si.click_submitbtn()
        self.assertEqual("My account - My Store",self.driver.title,"test_valid_signin---->FAILED")


############################ NEGATIVE TESTING ####################################


    def test_invalid_email_signin(self):
        si = Signin(self.driver)
        si.open_website(self.txturl)
        si.click_signinbtn()
        si.enter_valid_email(self.txtinvalidsigninemail)
        si.enter_valid_pwd(self.txtvalidsigninpwd)
        si.click_submitbtn()
        self.assertNotEqual("My account - My Store", self.driver.title, "test_invalid_email_signin---->FAILED")

    def test_invalid_pwd_signin(self):
        si = Signin(self.driver)
        si.open_website(self.txturl)
        si.click_signinbtn()
        si.enter_valid_email(self.txtvalidsigninemail)
        si.enter_valid_pwd(self.txtinvalidsigninpwd)
        si.click_submitbtn()
        self.assertNotEqual("My account - My Store", self.driver.title, "test_invalid_pwd_signin---->FAILED")

    def test_empty_email_signin(self):
        si = Signin(self.driver)
        si.open_website(self.txturl)
        si.click_signinbtn()
        si.enter_valid_email(self.txtemptysigninemail)
        si.enter_valid_pwd(self.txtvalidsigninpwd)
        si.click_submitbtn()
        self.assertNotEqual("My account - My Store", self.driver.title, "test_empty_email_signin----FAILED")

    def test_empty_pwd_signin(self):
        si = Signin(self.driver)
        si.open_website(self.txturl)
        si.click_signinbtn()
        si.enter_valid_email(self.txtvalidsigninemail)
        si.enter_valid_pwd(self.txtemptysigninpwd)
        si.click_submitbtn()
        self.assertNotEqual("My account - My Store", self.driver.title, "test_empty_pwd_signin---FAILED")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()



