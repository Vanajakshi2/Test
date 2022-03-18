from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

class Signup():

    #locators of all the elements in the page

    url = "http://automationpractice.com/index.php"
    browser = "chrome"
    signinbtn = "//div[@class='header_user_info']"
    creationemail = "email_create"
    createbtn = "//i[@class='icon-user left']"
    genderfemale = "id_gender2"
    gendermale = "id_gender1"
    firstname ="customer_firstname"
    lastname ="customer_lastname"
    email2 ="email"
    pwd = "passwd"
    day = "days"
    month = "months"
    year = "years"
    newsletter = "newsletter"
    offers = "optin"
    addfname = "firstname"
    addlname = "lastname"
    company = "company"
    address = "address1"
    address2="address2"
    city = "city"
    state = "id_state"
    pincode = "postcode"
    country = "id_country"
    info = "other"
    homephone = "phone"
    mobile_phone = "phone_mobile"
    alias = "alias"
    registerbtn = "submitAccount"

    ######################

    def __init__(self,txtdriver):
        self.driver=txtdriver

    def open_website(self, txturl):
        self.driver.get(txturl)



    def click_signinbtn(self):
        self.driver.find_element(By.XPATH, self.signinbtn).click()


    def enter_email(self,txtcreationemail):
        self.driver.find_element(By.ID, self.creationemail).clear()
        self.driver.find_element(By.ID, self.creationemail).send_keys(txtcreationemail)

    def enter_invalid_email(self, txtinvalidcreationemail):
        self.driver.find_element(By.ID, self.creationemail).clear()
        self.driver.find_element(By.ID, self.creationemail).send_keys(txtinvalidcreationemail)

    def enter_emptyemail(self,txtemptycreationemail):
        self.driver.find_element(By.ID, self.creationemail).clear()
        self.driver.find_element(By.ID, self.creationemail).send_keys(txtemptycreationemail)

    def click_createbtn(self):
        self.driver.find_element(By.XPATH,self.createbtn).click()

    def select_male_gender(self):
        time.sleep(4)
        self.driver.find_element(By.ID, self.gendermale).click()

    def select_female_gender(self):
        time.sleep(4)
        self.driver.find_element(By.ID, self.genderfemale).click()

    def enter_firstname(self,txtfirstname):
        self.driver.find_element(By.ID, self.firstname).clear()
        self.driver.find_element(By.ID, self.firstname).send_keys(txtfirstname)

    def enter_invalidfirstname(self,txtinvalidfirstname):
        self.driver.find_element(By.ID, self.firstname).clear()
        self.driver.find_element(By.ID, self.firstname).send_keys(txtinvalidfirstname)

    def enter_emptyfirstname(self,txtemptyfirstname):
        self.driver.find_element(By.ID, self.firstname).clear()
        self.driver.find_element(By.ID, self.firstname).send_keys(txtemptyfirstname)

    def enter_lastname(self, txtlastname):
        self.driver.find_element(By.ID, self.lastname).clear()
        self.driver.find_element(By.ID, self.lastname).send_keys(txtlastname)

    def enter_invalidlastname(self, txtinvalidlastname):
        self.driver.find_element(By.ID, self.lastname).clear()
        self.driver.find_element(By.ID, self.lastname).send_keys(txtinvalidlastname)

    def enter_emptylastname(self, txtemptylastname):
        self.driver.find_element(By.ID, self.lastname).clear()
        self.driver.find_element(By.ID, self.lastname).send_keys(txtemptylastname)

    def enter_pwd(self, txtpwd):
        self.driver.find_element(By.ID, self.pwd).clear()
        self.driver.find_element(By.ID, self.pwd).send_keys(txtpwd)

    def enter_invalidpwd(self, txtinvalidpwd):
        self.driver.find_element(By.ID, self.pwd).clear()
        self.driver.find_element(By.ID, self.pwd).send_keys(txtinvalidpwd)

    def enter_emptypwd(self, txtemptypwd):
        self.driver.find_element(By.ID, self.pwd).clear()
        self.driver.find_element(By.ID, self.pwd).send_keys(txtemptypwd)

    def select_dob(self):
        self.day = Select(self.driver.find_element(By.ID, self.day))
        self.day.select_by_value("10")
        self.month = Select(self.driver.find_element(By.ID, self.month))
        self.month.select_by_value("11")
        self.year = Select(self.driver.find_element(By.ID, self.year))
        self.year.select_by_value("1995")

    def select_checkboxes(self):
        self.driver.find_element(By.ID, self.newsletter).click()
        self.driver.find_element(By.ID, self.offers).click()
    def enter_company(self,txtcompany):
        self.driver.find_element(By.ID, self.company).clear()
        self.driver.find_element(By.ID, self.company).send_keys(txtcompany)

    def enter_address(self,txtaddress):
        self.driver.find_element(By.ID, self.address).clear()
        self.driver.find_element(By.ID, self.address).send_keys(txtaddress)

    def enter_empty_address(self,txtemptyaddress):
        self.driver.find_element(By.ID, self.address).clear()
        self.driver.find_element(By.ID, self.address).send_keys(txtemptyaddress)

    def enter_address2(self,txtaddress2):

        self.driver.find_element(By.ID, self.address2).clear()
        self.driver.find_element(By.ID, self.address2).send_keys(txtaddress2)

    def enter_city(self,txtcity):

        self.driver.find_element(By.ID, self.city).clear()
        self.driver.find_element(By.ID, self.city).send_keys(txtcity)

    def enter_invalid_city(self,txtinvalidcity):
        self.driver.find_element(By.ID, self.city).clear()
        self.driver.find_element(By.ID, self.city).send_keys(txtinvalidcity)

    def enter_empty_city(self,txtemptycity):
        self.driver.find_element(By.ID, self.city).clear()
        self.driver.find_element(By.ID, self.city).send_keys(txtemptycity)

    def select_state(self):

        self.state = Select(self.driver.find_element(By.ID, self.state))
        self.state.select_by_value("15")

    def enter_pincode(self,txtpincode):
        self.driver.find_element(By.ID, self.pincode).clear()
        self.driver.find_element(By.ID, self.pincode).send_keys(txtpincode)

    def enter_invalidpincode(self,txtinvalidpincode):
        self.driver.find_element(By.ID, self.pincode).clear()
        self.driver.find_element(By.ID, self.pincode).send_keys(txtinvalidpincode)

    def enter_emptypincode(self,txtemptypincode):
        self.driver.find_element(By.ID, self.pincode).clear()
        self.driver.find_element(By.ID, self.pincode).send_keys(txtemptypincode)

    def select_country(self):
        self.country = Select(self.driver.find_element(By.ID, self.country))
        self.country.select_by_value("21")

    def enter_txtinfo(self,txtinfo):
        self.driver.find_element(By.ID, self.info).clear()
        self.driver.find_element(By.ID, self.info).send_keys(txtinfo)

    def enter_mobilenumber(self, txtmobilephone):
        self.driver.find_element(By.ID, self.mobile_phone).send_keys(txtmobilephone)


    def enter_invalid_mobilenumber(self, txtinvalidmobilephone):
        self.driver.find_element(By.ID, self.mobile_phone).send_keys(txtinvalidmobilephone)

    def enter_empty_mobilenumber(self, txtemptymobilephone):
            self.driver.find_element(By.ID, self.mobile_phone).send_keys(txtemptymobilephone)

    def enter_homephone(self,txthomephone):
        self.driver.find_element(By.ID, self.homephone).send_keys(txthomephone)

    def enter_address_alias(self,txtalias):
        self.driver.find_element(By.ID, self.alias).clear()
        self.driver.find_element(By.ID, self.alias).send_keys(txtalias)


    def enter_empty_address_alias(self,txtemptyalias):
        self.driver.find_element(By.ID, self.alias).clear()
        self.driver.find_element(By.ID, self.alias).send_keys(txtemptyalias)


    def click_registerbtn(self):
        self.driver.find_element(By.ID, self.registerbtn).click()
        self.driver.quit()







