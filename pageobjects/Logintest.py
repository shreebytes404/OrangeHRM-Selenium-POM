from selenium.webdriver.common.by import By

#===============================
#PAGE OBJECT CLASS CREATION
#===============================
class LoginPage():
# ===============================
# LOCATORS FOR ALL THE ELEMENT
# ===============================
    textbox_username_name="username"
    textbox_password_name="password"
    button_login_xpath = "//button[@type='submit']"



#=================================
#SETTING THE CONSTRUCTOR
#=================================
    def __init__(self,driver):
        self.driver=driver


#=================================
#SETTING THE ACTION METHODS
#=================================

    def setUserName(self, username):
        self.driver.find_element(By.NAME, self.textbox_username_name).send_keys(username)


    def setPassword(self, password):
        self.driver.find_element(By.NAME, self.textbox_password_name).send_keys(password)


    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()



