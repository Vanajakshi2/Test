import unittest
from selenium import webdriver
import sys
import time
sys.path.append("C://Users/Vanajakshi/PycharmProjects/PythonUnitTestProject_POMBased")
from pageObjects.AssignmentSignupPageObject import Signup


class SignupTest(unittest.TestCase):
    txturl = "http://automationpractice.com/index.php"
    txtbrowser = "chrome"
    txtcreationemail = "sssss@vana.com"
    txtcreationemail2=  "sss22@sss.com"
    txtinvalidcreationemail="11111111111"
    txtfirstname ="Vanajakshi"
    txtinvalidfirstname=txtinvalidlastname =txtinvalidcity= "11111111111111"
    txtemptycreationemail=txtemptyfirstname=txtemptylastname=txtemptymobilenumber=txtemptyalias=txtemptycity=txtemptyaddress=txtemptypincode=txtemptyaddfname=txtemptyaddlname=" "
    txtlastname ="Kodavati"
    txtpwd = "123456789"
    txtinvalidpwd="111111"
    txtemptypwd=" "
    txtcompany = "comp"
    txtaddress = "add1"
    txtaddress2="add2"
    txtcity = "Hyd"
    txtpincode = "55555"
    txtinvalidpincode= txtinvalidmobilenumber="aaaaaa"
    txtinfo = "other"
    txthomephone = "999999999999"
    txtmobilephone = "999999999999"
    txtalias = "aliass"



    driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.txturl)
        cls.driver.maximize_window()

    def test_validsignup(self):
        su = Signup(self.driver)
        su.open_website(self.txturl)
        self.driver.implicitly_wait(4)
        su.click_signinbtn()
        su.enter_email(self.txtcreationemail)
        su.click_createbtn()
        time.sleep(3)
        su.select_female_gender()
        su.enter_firstname(self.txtfirstname)
        su.enter_lastname(self.txtlastname)
        su.enter_pwd(self.txtpwd)
        su.select_dob()
        su.select_checkboxes()
        su.enter_company(self.txtcompany)
        su.enter_address(self.txtaddress)
        su.enter_city(self.txtcity)
        su.select_state()
        su.enter_pincode(self.txtpincode)
        su.select_country()
        su.enter_txtinfo(self.txtinfo)
        su.enter_homephone(self.txthomephone)
        su.enter_mobilenumber(self.txtmobilephone)
        su.enter_address_alias(self.txtalias)
        su.click_registerbtn()
        time.sleep(4)
        self.assertEqual("My account -My Store",self.driver.title, "SIGNUP FAILED")

    def test_invalidmailsignup(self):
        su = Signup(self.driver)
        self.driver.implicitly_wait(4)
        su.open_website(self.txturl)
        su.click_signinbtn()
        su.enter_invalid_email(self.txtinvalidcreationemail)
        su.click_createbtn()
        self.assertNotEqual("My account -My Store",self.driver.title, "test_invalidmailsignup- FAILED")

    def test_invalidfirstname_signup(self):
        su = Signup(self.driver)
        su.open_website(self.txturl)
        self.driver.implicitly_wait(4)
        su.click_signinbtn()
        su.enter_email(self.txtcreationemail2)
        su.click_createbtn()
        time.sleep(4)
        su.select_female_gender()
        su.enter_invalidfirstname(self.txtinvalidfirstname)
        su.enter_lastname(self.txtlastname)
        su.enter_pwd(self.txtpwd)
        su.select_dob()
        su.select_checkboxes()
        su.enter_company(self.txtcompany)
        su.enter_address(self.txtaddress)
        su.enter_city(self.txtcity)
        su.select_state()
        su.enter_pincode(self.txtpincode)
        su.select_country()
        su.enter_txtinfo(self.txtinfo)
        su.enter_homephone(self.txthomephone)
        su.enter_mobilenumber(self.txtmobilephone)
        su.enter_address_alias(self.txtalias)
        su.click_registerbtn()
        time.sleep(4)
        self.assertNotEqual("My account -My Store",self.driver.title, "test_invalidfirstname_signup-FAILED")


    def test_invalidlastname_signup(self):
        su = Signup(self.driver)
        su.open_website(self.txturl)
        self.driver.implicitly_wait(4)
        su.click_signinbtn()
        su.enter_email(self.txtcreationemail2)
        su.click_createbtn()
        time.sleep(3)
        su.select_female_gender()
        su.enter_firstname(self.txtfirstname)
        su.enter_invalidlastname(self.txtinvalidlastname)
        su.enter_pwd(self.txtpwd)
        su.select_dob()
        su.select_checkboxes()
        su.enter_company(self.txtcompany)
        su.enter_address(self.txtaddress)
        su.enter_city(self.txtcity)
        su.select_state()
        su.enter_pincode(self.txtpincode)
        su.select_country()
        su.enter_txtinfo(self.txtinfo)
        su.enter_homephone(self.txthomephone)
        su.enter_mobilenumber(self.txtmobilephone)
        su.enter_address_alias(self.txtalias)
        su.click_registerbtn()
        time.sleep(4)
        self.assertNotEqual("My account -My Store",self.driver.title, "test_invalidlastname_signup-FAILED")


    def test_invalidpwd_signup(self):
        su = Signup(self.driver)
        su.open_website(self.txturl)
        self.driver.implicitly_wait(4)
        su.click_signinbtn()
        su.enter_email(self.txtcreationemail2)
        su.click_createbtn()
        time.sleep(3)
        su.select_female_gender()
        su.enter_firstname(self.txtfirstname)
        su.enter_lastname(self.txtlastname)
        su.enter_invalidpwd(self.txtinvalidpwd)
        su.select_dob()
        su.select_checkboxes()
        su.enter_company(self.txtcompany)
        su.enter_address(self.txtaddress)
        su.enter_city(self.txtcity)
        su.select_state()
        su.enter_pincode(self.txtpincode)
        su.select_country()
        su.enter_txtinfo(self.txtinfo)
        su.enter_homephone(self.txthomephone)
        su.enter_mobilenumber(self.txtmobilephone)
        su.enter_address_alias(self.txtalias)
        su.click_registerbtn()
        time.sleep(4)
        self.assertNotEqual("My account -My Store",self.driver.title, "test_invalidpwd_signup-FAILED")



    def test_invaliddob_signup(self):
        su = Signup(self.driver)
        su.open_website(self.txturl)
        self.driver.implicitly_wait(4)
        su.click_signinbtn()
        su.enter_email(self.txtcreationemail2)
        su.click_createbtn()
        time.sleep(3)
        su.select_female_gender()
        su.enter_firstname(self.txtfirstname)
        su.enter_lastname(self.txtlastname)
        su.enter_invalidpwd(self.txtpwd)
        su.select_invaliddob()
        su.select_checkboxes()
        su.enter_company(self.txtcompany)
        su.enter_address(self.txtaddress)
        su.enter_city(self.txtcity)
        su.select_state()
        su.enter_pincode(self.txtpincode)
        su.select_country()
        su.enter_txtinfo(self.txtinfo)
        su.enter_homephone(self.txthomephone)
        su.enter_mobilenumber(self.txtmobilephone)
        su.enter_address_alias(self.txtalias)
        su.click_registerbtn()
        time.sleep(4)
        self.assertNotEqual("My account -My Store",self.driver.title, "test_invalidpwd_signup-FAILED")



    def test_invalidcity_signup(self):
        su = Signup(self.driver)
        su.open_website(self.txturl)
        self.driver.implicitly_wait(4)
        su.click_signinbtn()
        su.enter_email(self.txtcreationemail2)
        su.click_createbtn()
        time.sleep(3)
        su.select_female_gender()
        su.enter_firstname(self.txtfirstname)
        su.enter_lastname(self.txtlastname)
        su.enter_pwd(self.txtpwd)
        su.select_dob()
        su.select_checkboxes()
        su.enter_company(self.txtcompany)
        su.enter_address(self.txtaddress)
        su.enter_invalid_city(self.txtinvalidcity)
        su.select_state()
        su.enter_pincode(self.txtpincode)
        su.select_country()
        su.enter_txtinfo(self.txtinfo)
        su.enter_homephone(self.txthomephone)
        su.enter_mobilenumber(self.txtmobilephone)
        su.enter_address_alias(self.txtalias)
        su.click_registerbtn()
        time.sleep(4)
        self.assertNotEqual("My account -My Store",self.driver.title, "test_invalidcity_signup-FAILED")


    def test_invalidpincode_signup(self):
        su = Signup(self.driver)
        su.open_website(self.txturl)
        self.driver.implicitly_wait(4)
        su.click_signinbtn()
        su.enter_email(self.txtcreationemail2)
        su.click_createbtn()
        time.sleep(3)
        su.select_female_gender()
        su.enter_firstname(self.txtfirstname)
        su.enter_lastname(self.txtlastname)
        su.enter_pwd(self.txtpwd)
        su.select_dob()
        su.select_checkboxes()
        su.enter_company(self.txtcompany)
        su.enter_address(self.txtaddress)
        su.enter_city(self.txtcity)
        su.select_state()
        su.enter_invalidpincode(self.txtinvalidpincode)
        su.select_country()
        su.enter_txtinfo(self.txtinfo)
        su.enter_homephone(self.txthomephone)
        su.enter_mobilenumber(self.txtmobilephone)
        su.enter_address_alias(self.txtalias)
        su.click_registerbtn()
        time.sleep(4)
        self.assertNotEqual("My account -My Store",self.driver.title, "test_invalidpincode_signup-FAILED")



    def test_invalidmobilephone_signup(self):
        su = Signup(self.driver)
        su.open_website(self.txturl)
        self.driver.implicitly_wait(4)
        su.click_signinbtn()
        su.enter_email(self.txtcreationemail2)
        su.click_createbtn()
        time.sleep(3)
        su.select_female_gender()
        su.enter_firstname(self.txtfirstname)
        su.enter_lastname(self.txtlastname)
        su.enter_pwd(self.txtpwd)
        su.select_dob()
        su.select_checkboxes()
        su.enter_company(self.txtcompany)
        su.enter_address(self.txtaddress)
        su.enter_city(self.txtcity)
        su.select_state()
        su.enter_pincode(self.txtpincode)
        su.select_country()
        su.enter_txtinfo(self.txtinfo)
        su.enter_homephone(self.txthomephone)
        su.enter_invalid_mobilenumber(self.txtinvalidmobilenumber)
        su.enter_address_alias(self.txtalias)
        su.click_registerbtn()
        time.sleep(4)
        self.assertNotEqual("My account -My Store",self.driver.title, "test_invalidmobilephone_signup-FAILED")

    def test_empty_email_signup(self):

         su = Signup(self.driver)
         su.open_website(self.txturl)
         self.driver.implicitly_wait(4)
         su.click_signinbtn()
         su.enter_emptyemail(self.txtemptycreationemail)
         self.assertNotEqual("My account -My Store", self.driver.title, "test_empty_email_signup-FAILED")


    def test_emptyfirstname_signup(self):
        su = Signup(self.driver)
        su.open_website(self.txturl)
        self.driver.implicitly_wait(4)
        su.click_signinbtn()
        su.enter_email(self.txtcreationemail2)
        su.click_createbtn()
        time.sleep(3)
        su.select_female_gender()
        su.enter_emptyfirstname(self.txtemptyfirstname)
        su.enter_lastname(self.txtlastname)
        su.enter_pwd(self.txtpwd)
        su.select_dob()
        su.select_checkboxes()
        su.enter_company(self.txtcompany)
        su.enter_address(self.txtaddress)
        su.enter_city(self.txtcity)
        su.select_state()
        su.enter_pincode(self.txtpincode)
        su.select_country()
        su.enter_txtinfo(self.txtinfo)
        su.enter_homephone(self.txthomephone)
        su.enter_mobilenumber(self.txtmobilephone)
        su.enter_address_alias(self.txtalias)
        su.click_registerbtn()
        time.sleep(4)
        self.assertNotEqual("My account -My Store",self.driver.title, "test_emptyfirstname_signup-FAILED")



    def test_emptylastname_signup(self):
        su = Signup(self.driver)
        su.open_website(self.txturl)
        self.driver.implicitly_wait(4)
        su.click_signinbtn()
        su.enter_email(self.txtcreationemail2)
        su.click_createbtn()
        time.sleep(3)
        su.select_female_gender()
        su.enter_firstname(self.txtfirstname)
        su.enter_emptylastname(self.txtemptylastname)
        su.enter_pwd(self.txtpwd)
        su.select_dob()
        su.select_checkboxes()
        su.enter_company(self.txtcompany)
        su.enter_address(self.txtaddress)
        su.enter_city(self.txtcity)
        su.select_state()
        su.enter_pincode(self.txtpincode)
        su.select_country()
        su.enter_txtinfo(self.txtinfo)
        su.enter_homephone(self.txthomephone)
        su.enter_mobilenumber(self.txtmobilephone)
        su.enter_address_alias(self.txtalias)
        su.click_registerbtn()
        time.sleep(4)
        self.assertNotEqual("My account -My Store",self.driver.title, "test_emptylastname_signup-FAILED")


    def test_emptypwd_signup(self):
        su = Signup(self.driver)
        su.open_website(self.txturl)
        self.driver.implicitly_wait(4)
        su.click_signinbtn()
        su.enter_email(self.txtcreationemail2)
        su.click_createbtn()
        time.sleep(3)
        su.select_female_gender()
        su.enter_firstname(self.txtfirstname)
        su.enter_lastname(self.txtlastname)
        su.enter_emptypwd(self.txtemptypwd)
        su.select_dob()
        su.select_checkboxes()
        su.enter_company(self.txtcompany)
        su.enter_address(self.txtaddress)
        su.enter_city(self.txtcity)
        su.select_state()
        su.enter_pincode(self.txtpincode)
        su.select_country()
        su.enter_txtinfo(self.txtinfo)
        su.enter_homephone(self.txthomephone)
        su.enter_mobilenumber(self.txtmobilephone)
        su.enter_address_alias(self.txtalias)
        su.click_registerbtn()
        time.sleep(4)
        self.assertNotEqual("My account -My Store",self.driver.title, "test_emptypwd_signup-FAILED")


    def test_emptyaddress_signup(self):
        su = Signup(self.driver)
        su.open_website(self.txturl)
        self.driver.implicitly_wait(4)
        su.click_signinbtn()
        su.enter_email(self.txtcreationemail2)
        su.click_createbtn()
        time.sleep(3)
        su.select_female_gender()
        su.enter_firstname(self.txtfirstname)
        su.enter_lastname(self.txtlastname)
        su.enter_pwd(self.txtpwd)
        su.select_dob()
        su.select_checkboxes()
        su.enter_company(self.txtcompany)
        su.enter_empty_address(self.txtemptyaddress)
        su.enter_city(self.txtcity)
        su.select_state()
        su.enter_pincode(self.txtpincode)
        su.select_country()
        su.enter_txtinfo(self.txtinfo)
        su.enter_homephone(self.txthomephone)
        su.enter_mobilenumber(self.txtmobilephone)
        su.enter_address_alias(self.txtalias)
        su.click_registerbtn()
        time.sleep(4)
        self.assertNotEqual("My account -My Store",self.driver.title, "test_emptyaddress_signup-FAILED")

    def test_emptypincode_signup(self):
        su = Signup(self.driver)
        su.open_website(self.txturl)
        self.driver.implicitly_wait(4)
        su.click_signinbtn()
        su.enter_email(self.txtcreationemail2)
        su.click_createbtn()
        time.sleep(3)
        su.select_female_gender()
        su.enter_firstname(self.txtfirstname)
        su.enter_lastname(self.txtlastname)
        su.enter_pwd(self.txtpwd)
        su.select_dob()
        su.select_checkboxes()
        su.enter_company(self.txtcompany)
        su.enter_address(self.txtemptyaddress)
        su.enter_city(self.txtcity)
        su.select_state()
        su.enter_emptypincode(self.txtemptypincode)
        su.select_country()
        su.enter_txtinfo(self.txtinfo)
        su.enter_homephone(self.txthomephone)
        su.enter_mobilenumber(self.txtmobilephone)
        su.enter_address_alias(self.txtalias)
        su.click_registerbtn()
        time.sleep(4)
        self.assertNotEqual("My account -My Store", self.driver.title, "test_emptypincode_signup-FAILED")

    def test_emptymobilenumber_signup(self):
        su = Signup(self.driver)
        su.open_website(self.txturl)
        self.driver.implicitly_wait(4)
        su.click_signinbtn()
        su.enter_email(self.txtcreationemail2)
        su.click_createbtn()
        time.sleep(3)
        su.select_female_gender()
        su.enter_firstname(self.txtfirstname)
        su.enter_lastname(self.txtlastname)
        su.enter_pwd(self.txtpwd)
        su.select_dob()
        su.select_checkboxes()
        su.enter_company(self.txtcompany)
        su.enter_address(self.txtaddress)
        su.enter_city(self.txtcity)
        su.select_state()
        su.enter_pincode(self.txtpincode)
        su.select_country()
        su.enter_txtinfo(self.txtinfo)
        su.enter_homephone(self.txthomephone)
        su.enter_empty_mobilenumber(self.txtemptymobilenumber)
        su.enter_address_alias(self.txtalias)
        su.click_registerbtn()
        time.sleep(4)
        self.assertNotEqual("My account -My Store", self.driver.title, "test_emptymobilenumber_signup-FAILED")

    def test_emptyalias_signup(self):
        su = Signup(self.driver)
        su.open_website(self.txturl)
        self.driver.implicitly_wait(4)
        su.click_signinbtn()
        su.enter_email(self.txtcreationemail2)
        su.click_createbtn()
        time.sleep(3)
        su.select_female_gender()
        su.enter_firstname(self.txtfirstname)
        su.enter_lastname(self.txtlastname)
        su.enter_pwd(self.txtpwd)
        su.select_dob()
        su.select_checkboxes()
        su.enter_company(self.txtcompany)
        su.enter_address(self.txtaddress)
        su.enter_city(self.txtcity)
        su.select_state()
        su.enter_pincode(self.txtpincode)
        su.select_country()
        su.enter_txtinfo(self.txtinfo)
        su.enter_homephone(self.txthomephone)
        su.enter_mobilenumber(self.txtmobilephone)
        su.enter_empty_address_alias(self.txtemptyalias)
        su.click_registerbtn()
        time.sleep(4)
        self.assertNotEqual("My account -My Store", self.driver.title, "test_emptyalias_signup-FAILED")


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__=="__main__":
    unittest.main()


