import unittest
import time
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from Project_demoautomationtesting.POM.signup_page import signup
from Project_demoautomationtesting.POM.Register_page import Register
from Project_demoautomationtesting.POM.practicesite_page import practice


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="/Users/aarviaditya/Desktop/Testing/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_project(self):
        driver = self.driver
        driver.get("http://demo.automationtesting.in")

        signuppage = signup(driver)
        signuppage.click_signup()

        register = Register(driver)
        register.text_name("Harry")
        register.text_lastname("Porter")
        register.text_address("Magic Land","vish.mittal@gmail.com","6454448989")
        register.click_gender_hobbies()
        register.text_language()
        register.link_skills()
        register.link_country()
        register.link_date()
        register.text_password("Testing789","Testing789")
        register.click_submit()

        Practice = practice(driver)
        Practice.click_practice()
        Practice.click_product()


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/aarviaditya/Desktop/Testing/HTML1_Python"),verbosity=2)

