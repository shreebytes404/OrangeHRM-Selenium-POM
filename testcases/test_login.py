#===============================
#        ALL IMPORTS
#===============================
import time
import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import sys
sys.path.append(r"C:\Users\HP\PycharmProjects\POM_")

from pageobjects.Logintest import LoginPage

service = Service(r"C:\Users\HP\geckodriver-v0.36.0-win32\geckodriver.exe")

#===============================
#         TEST  CLASS
#===============================
class HomePagetest(unittest.TestCase):

#===============================
#         TEST  DATA
#===============================
    baseURL="https://opensource-demo.orangehrmlive.com/"
    username=("Admin")
    password=("admin123")
    driver = webdriver.Firefox(service=service)


#===============================
#       PRE-CONDITIONS
#===============================
    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        time.sleep(5)

#===============================
#          TEST  CASE
#===============================

    def test_homepage(self):
        lp=LoginPage(self.driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        time.sleep(5)
        self.assertEqual("OrangeHRM", self.driver.title,"title is not matching!!")


#===============================
#         POST-CONDITIONS
#===============================
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

#==============================
#       TEST  EXECUTION
#==============================

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=r"C:\\Users\\HP\\PycharmProjects\\POM_\\reports"))
