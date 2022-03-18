import unittest
from selenium import webdriver
import sys
import time
sys.path.append("C://Users/Vanajakshi/PycharmProjects/PythonUnitTestProject_POMBased")
from pageObjects.AssignmentFlowPageObject import Flow


class FlowTest(unittest.TestCase):
    txturl = "http://automationpractice.com/index.php"
    txtbrowser = "chrome"
    txtvalidsigninemail = "kodavativanajakshi1@gmail.com"
    txtinvalidsigninemail="aaaaaaaaaaaa"
    txtvalidsigninpwd = "1234567"
    txtinvalidsigninpwd= "  "
    driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.txturl)
        cls.driver.maximize_window()


    def test_validuser_quickview_buyitem(self):

        fl=Flow(self.driver)
        fl.open_website(self.txturl)
        fl.click_signinbtn()
        fl.enter_valid_email(self.txtvalidsigninemail)
        fl.enter_valid_pwd(self.txtvalidsigninpwd)
        fl.click_submitbtn()
        self.assertEqual("My account - My Store",self.driver.title,"SIGNIN FAILED")
        fl.select_catagory()
        fl.select_filters()
        fl.quick_view_product()
        fl.modify_product_properties()
        fl.add_to_cart()
        time.sleep(4)
        fl.proceed_to_checkout()
        fl.confirm_summary()
        fl.confirm_address()
        fl.confirm_shipping()
        fl.confirm_payment()
        fl.confirm_order()
        self.assertEqual("Order confirmation - My Store",self.driver.title,"PRODUCT ORDERING FAILED")


    def test_validuser_continueshopping_buyitem(self):

        fl=Flow(self.driver)
        fl.open_website(self.txturl)
        fl.click_signinbtn()
        time.sleep(4)
        fl.enter_valid_email(self.txtvalidsigninemail)
        fl.enter_valid_pwd(self.txtvalidsigninpwd)
        fl.click_submitbtn()
        self.assertEqual("My account - My Store",self.driver.title,"SIGNIN FAILED")
        fl.select_catagory()
        fl.select_filters()
        fl.quick_view_product()
        fl.modify_product_properties()
        fl.add_to_cart()
        time.sleep(4)
        fl.continue_shopping()
        fl.select_catagory()
        time.sleep(4)
        fl.quick_productcontainer_addtocart()
        time.sleep(4)
        fl.proceed_to_checkout()
        fl.confirm_summary()
        fl.confirm_address()
        fl.confirm_shipping()
        fl.confirm_payment()
        fl.confirm_order()
        self.assertEqual("Order confirmation - My Store",self.driver.title,"PRODUCT ORDERING FAILED")

    def test_buyitems_fromcart(self):

        fl=Flow(self.driver)
        fl.open_website(self.txturl)
        fl.click_signinbtn()
        fl.enter_valid_email(self.txtvalidsigninemail)
        fl.enter_valid_pwd(self.txtvalidsigninpwd)
        fl.click_submitbtn()
        self.assertEqual("My account - My Store",self.driver.title,"SIGNIN FAILED")
        fl.select_catagory()
        fl.select_filters()
        fl.quick_view_product()
        fl.modify_product_properties()
        fl.add_to_cart()
        time.sleep(8)
        fl.container_checkout_closewindow()
        self.driver.implicitly_wait(4)
        fl.cart_checkout()
        time.sleep(5)
        fl.confirm_summary()
        fl.confirm_address()
        fl.confirm_shipping()
        fl.confirm_payment()
        fl.confirm_order()
        self.assertEqual("Order confirmation - My Store", self.driver.title, "PRODUCT ORDERING FAILED")

    def test_search_buyitem(self):
        fl = Flow(self.driver)

        fl.open_website(self.txturl)
        fl.click_signinbtn()
        fl.enter_valid_email(self.txtvalidsigninemail)
        fl.enter_valid_pwd(self.txtvalidsigninpwd)
        fl.click_submitbtn()
        self.assertEqual("My account - My Store",self.driver.title,"SIGNIN FAILED")
        fl.searchitem()
        fl.select_searched_product()
        fl.add_to_cart()
        time.sleep(4)
        fl.proceed_to_checkout()
        fl.confirm_summary()
        fl.confirm_address()
        fl.confirm_shipping()
        fl.confirm_payment()
        fl.confirm_order()
        self.assertEqual("Order confirmation - My Store",self.driver.title,"PRODUCT ORDERING FAILED")



    def deleteitems_from_cart(self):

        fl=Flow(self.driver)
        fl.open_website(self.txturl)
        fl.click_signinbtn()
        fl.enter_valid_email(self.txtvalidsigninemail)
        fl.enter_valid_pwd(self.txtvalidsigninpwd)
        fl.click_submitbtn()
        self.assertEqual("My account - My Store",self.driver.title,"SIGNIN FAILED")
        fl.select_catagory()
        fl.quick_productcontainer_addtocart()
        fl.continue_shopping()
        fl.quick_productcontainer_addtocart()
        fl.container_checkout_closewindow()
        fl.cart_delete()
        self.assertNotEqual("Order confirmation - My Store", self.driver.title, "DELETION FAILED")

    def deleteitems_from_summarypage(self):
        fl = Flow(self.driver)
        fl.open_website(self.txturl)
        fl.click_signinbtn()
        fl.enter_valid_email(self.txtvalidsigninemail)
        fl.enter_valid_pwd(self.txtvalidsigninpwd)
        fl.click_submitbtn()
        self.assertEqual("My account - My Store", self.driver.title, "SIGNIN FAILED")
        fl.select_catagory()
        fl.quick_productcontainer_addtocart()
        fl.continue_shopping()
        fl.quick_productcontainer_addtocart()
        fl.container_checkout_closewindow()
        fl.cart_checkout()
        fl.delete_checkout()
        self.assertNotEqual("Order confirmation - My Store", self.driver.title, "DELETION FAILED")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__=="__main__":
    unittest.main()
