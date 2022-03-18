from selenium.webdriver.common.by import By

class Signin():

    #locators of all the elements in the page
    url = "http://automationpractice.com/index.php"
    browser = "chrome"
    signinbtn = "//div[@class='header_user_info']"
    signinemail = "email"
    signinpwd = "passwd"
    signinsubmit = "SubmitLogin"

    def __init__(self,txtdriver):
        self.driver=txtdriver

    def open_website(self, txturl):
        self.driver.get(txturl)

    def click_signinbtn(self):
        self.driver.find_element(By.XPATH, self.signinbtn).click()

    def enter_valid_email(self, txtvalidsigninemail):
        self.driver.find_element(By.ID, self.signinemail).clear()
        self.driver.find_element(By.ID, self.signinemail).send_keys(txtvalidsigninemail)

    def enter_valid_pwd(self, txtvalidsigninpwd):
        self.driver.find_element(By.ID, self.signinpwd).clear()
        self.driver.find_element(By.ID, self.signinpwd).send_keys(txtvalidsigninpwd)

    def enter_invalid_email(self, txtinvalidsigninemail):
        self.driver.find_element(By.ID, self.signinemail).clear()
        self.driver.find_element(By.ID, self.signinemail).send_keys(txtinvalidsigninemail)

    def enter_invalid_pwd(self, txtinvalidsigninpwd):
        self.driver.find_element(By.ID, self.signinpwd).clear()
        self.driver.find_element(By.ID, self.signinpwd).send_keys(txtinvalidsigninpwd)

    def click_submitbtn(self):
        self.driver.find_element(By.ID, self.signinsubmit).click()
        print(self.driver.title)


################################################################################
    #
    # def click_signinbtn(self):
    #     self.driver.find_element(By.XPATH, self.signinbtn).click()
    #
    #
    # def enter_logindetails(self,txtsigninemail,txtsigninpwd):
    #     self.driver.find_element(By.ID, self.signinemail).clear()
    #     self.driver.find_element(By.ID, self.signinemail).send_keys(txtsigninemail)
    #     self.driver.find_element(By.ID, self.signinpwd).clear()
    #     self.driver.find_element(By.ID, self.signinpwd).send_keys(txtsigninpwd)
    #     self.driver.find_element(By.ID, self.signinsubmit).click()
    #     print(self.driver.title)
    #
