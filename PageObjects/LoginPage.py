from selenium import webdriver
class Login:
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_Xpath = "//input[@class='button-1 login-button' and @type='submit']"
    link_logout_linktext = "//a[contains(text(),'Logout')]"

    def __init__(self,driver):
        self.driver = driver

    def setUserName(self,username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)
    
    def setPassword(self,psaaword):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(psaaword)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_Xpath).click()

    def clickLogout(self):
        #self.driver.find_element_by_link_text(self.link_logout_linktext).click()
        self.driver.find_element_by_xpath(self.link_logout_linktext).click()