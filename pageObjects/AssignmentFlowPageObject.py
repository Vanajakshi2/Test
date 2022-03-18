from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver import ActionChains

class Flow():

    #locators of all the elements in the page
    url = "http://automationpractice.com/index.php"
    browser = "chrome"
    signinbtn = "//div[@class='header_user_info']"
    signinemail = "email"
    signinpwd = "passwd"
    signinsubmit = "SubmitLogin"
    women = "//a[@title='Women']"
    Tshirts = "//ul[@class='submenu-container clearfix first-in-line-xs']//a[@title='T-shirts']"
    size = "layered_id_attribute_group_2"
    color = "layered_id_attribute_group_14"
    composition = "layered_id_feature_5"
    styles = "layered_id_feature_11"
    properties = "layered_id_feature_17"
    availability = "layered_quantity_1"
    manufacturer = "layered_manufacturer_1"
    condition = "layered_condition_new"
    quickview = "//li[@class='ajax_block_product col-xs-12 col-sm-6 col-md-4 first-in-line last-line first-item-of-tablet-line first-item-of-mobile-line last-mobile-line']"
    quickproductcontainer="//div[@class='product-container']"
    quickaddtocart="//div[@class='button-container']/a[@title='Add to cart']"
    quantity = "//*[@class='btn btn-default button-plus product_quantity_up']"
    sizee = "group_1"
    colorr = "color_13"
    addtocart = "//button[@name='Submit']"
    proceedtocheckout1 = "//*[@title='Proceed to checkout']"
    summarycheckout = "//p[@class='cart_navigation clearfix']//a[@title='Proceed to checkout']"
    addresscheckout = "//*[@name='processAddress']"
    terms = "cgv"
    shippingcheckout = "//*[@name='processCarrier']"
    payment = "//*[@title='Pay by bank wire']"
    confirmorder = "//p[@class='cart_navigation clearfix']/button[@type='submit']"
    searchitem="search_query_top"
    searchbutton="//button[@name='submit_search']"
    searchproduct="//*[@id='center_column']/ul/li[1]/div/div[1]/div/a[1]/img"



    def __init__(self,txtdriver):
        self.driver=txtdriver

    def open_website(self,txturl):
        self.driver.get(txturl)

    def click_signinbtn(self):
        self.driver.find_element(By.XPATH, self.signinbtn).click()

    def enter_valid_email(self,txtvalidsigninemail):
        self.driver.find_element(By.ID, self.signinemail).clear()
        self.driver.find_element(By.ID, self.signinemail).send_keys(txtvalidsigninemail)

    def enter_valid_pwd(self,txtvalidsigninpwd):
        self.driver.find_element(By.ID, self.signinpwd).clear()
        self.driver.find_element(By.ID, self.signinpwd).send_keys(txtvalidsigninpwd)

    def click_submitbtn(self):
        self.driver.find_element(By.ID, self.signinsubmit).click()

    def select_catagory(self):
        self.mouse = ActionChains(self.driver)
        self.women = self.driver.find_element(By.XPATH, "//a[@title='Women']")
        self.Tshirts = self.driver.find_element(By.XPATH,"//ul[@class='submenu-container clearfix first-in-line-xs']//a[@title='T-shirts']")
        self.mouse.move_to_element(self.women).move_to_element(self.Tshirts).click().perform()

    def select_filters(self):
        self.driver.find_element(By.ID, "layered_id_attribute_group_2").click()
        self.driver.find_element(By.ID, "layered_id_attribute_group_14").click()
        self.driver.find_element(By.ID, "layered_id_feature_5").click()
        self.driver.find_element(By.ID, "layered_id_feature_11").click()
        self.driver.find_element(By.ID, "layered_id_feature_17").click()
        self.driver.find_element(By.ID, "layered_quantity_1").click()
        self.driver.find_element(By.ID, "layered_condition_new").click()

    def quick_view_product(self):
        self.driver.find_element(By.XPATH, "//li[@class='ajax_block_product col-xs-12 col-sm-6 col-md-4 first-in-line last-line first-item-of-tablet-line first-item-of-mobile-line last-mobile-line']").click()

    def modify_product_properties(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[@class='btn btn-default button-plus product_quantity_up']")
        self.size = Select(self.driver.find_element(By.ID, "group_1"))
        self.size.select_by_value("2")
        self.driver.find_element(By.ID, "color_13").click()

    def add_to_cart(self):
        self.driver.find_element(By.XPATH, "//button[@name='Submit']").click()

    def proceed_to_checkout(self):
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//*[@title='Proceed to checkout']").click()

    def continue_shopping(self):
        self.continueshopping=self.driver.find_element(By.XPATH,"//span[@title='Continue shopping']")
        wait=WebDriverWait(self.driver,10)
        wait.until(ec.element_to_be_clickable(self.continueshopping))
        self.continueshopping.click()
    def quick_productcontainer_addtocart(self):

        self.container=self.driver.find_element(By.XPATH,"//div[@class='product-container']")
        self.containeraddtocart=self.driver.find_element(By.XPATH,"//div[@class='button-container']/a[@title='Add to cart']")
        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.presence_of_element_located(self.container))
        wait.until(ec.presence_of_element_located(self.containeraddtocart))
        self.mouse = ActionChains(self.driver).move_to_element(self.container).move_to_element(self.containeraddtocart).click().perform()

    def container_checkout_closewindow(self):
        self.driver.find_element(By.XPATH,"//span[@title='Close window']").click()


    def confirm_summary(self):
        self.driver.find_element(By.XPATH, "//p[@class='cart_navigation clearfix']//a[@title='Proceed to checkout']").click()

    def confirm_address(self):
        self.driver.find_element(By.XPATH, "//*[@name='processAddress']").click()

    def confirm_shipping(self):
        self.driver.find_element(By.ID, "cgv").click()
        self.driver.find_element(By.XPATH, "//*[@name='processCarrier']").click()


    def cart_checkout(self):
        self.cart = self.driver.find_element(By.XPATH, "//a[@title='View my shopping cart']")
        self.cartcheckout=self.driver.find_element(By.ID,"button_order_cart")
        self.mouse=ActionChains(self.driver).move_to_element(self.cart).move_to_element(self.cartcheckout).click()

    def search_item(self):
        self.searchbar=self.driver.find_element(By.ID,self.searchitem)
        self.searchbar.send_key("dresses")
        self.searchbtn=self.driver.find_element(By.XPATH,self.searchbutton)
        self.searchbtn.click()

    def select_searched_product(self):
        self.driver.find_element(By.XPATH,self.searchproduct).click()



    def cart_delete(self):
        self.cart = self.driver.find_element(By.XPATH, "//a[@title='View my shopping cart']")
        self.delete=self.driver.find_element(By.XPATH,"//a[@title='remove this product from my cart']")

    def delete_checkout(self):
        self.driver.find_element(By.XPATH,"//a[@title='Delete']").click()


    def confirm_payment(self):
        self.driver.find_element(By.XPATH, "//*[@title='Pay by bank wire']").click()

    def confirm_order(self):
        self.driver.find_element(By.XPATH, "//p[@class='cart_navigation clearfix']/button[@type='submit']").click()




