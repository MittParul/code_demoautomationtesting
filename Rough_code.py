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



class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
            cls.driver = webdriver.Chrome(executable_path="/Users/aarviaditya/Desktop/Testing/chromedriver.exe")
            cls.driver.implicitly_wait(10)
            cls.driver.maximize_window()


    def test_Register(self):
        self.driver.get("http://demo.automationtesting.in")
        self.driver.find_element_by_xpath("//img[@id='enterimg']").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//input[@placeholder='First Name']").send_keys("Harry")
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//input[@placeholder='Last Name']").send_keys("Porter")
        self.driver.find_element_by_xpath("/html[1]/body[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[2]/div[1]/textarea[1]").send_keys("Magic Land")
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("/html[1]/body[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[3]/div[1]/input[1]").send_keys("vish.mittal@gmail.com")
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("/html[1]/body[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[4]/div[1]/input[1]").send_keys("6454448989")
        self.driver.find_element_by_xpath("//label[1]//input[1]").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//input[@id='checkbox2']").click()
        self.driver.find_element_by_xpath("//div[@id='msdd']").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//a[contains(text(),'English')]").click()
        self.driver.implicitly_wait(10)
        skills = self.driver.find_element_by_xpath("//select[@id='Skills']")
        drp = Select(skills)
        drp.select_by_visible_text("Analytics")
        self.driver.implicitly_wait(10)
        country = self.driver.find_element_by_xpath("// select[ @ id = 'countries']")
        drp1 = Select(country)
        drp1.select_by_visible_text("Australia")
        self.driver.implicitly_wait(10)
        year = self.driver.find_element_by_xpath("// select[ @ id = 'yearbox']")
        drp2 = Select(year)
        drp2.select_by_visible_text("1982")
        self.driver.implicitly_wait(10)
        month = self.driver.find_element_by_xpath("//select[@placeholder='Month']")
        drp3 = Select(month)
        drp3.select_by_visible_text("January")
        self.driver.implicitly_wait(10)
        day = self.driver.find_element_by_xpath("//select[@id='daybox']")
        drp4 = Select(day)
        drp4.select_by_visible_text("18")
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//input[@id='firstpassword']").send_keys("Testing789")
        self.driver.find_element_by_xpath("//input[@id='secondpassword']").send_keys("Testing789")
        self.driver.find_element_by_xpath("//button[@id='submitbtn']").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("// a[contains(text(), 'Practice Site')]").click()
        time.sleep(10)
        self.driver.execute_script("window.scrollBy(0,750)", "")
        time.sleep(5)
        self.driver.find_element_by_xpath("// h3[contains(text(), 'Thinking in HTML')]").click()
        self.driver.find_element_by_xpath("// button[@class ='single_add_to_cart_button button alt']").click()
        self.driver.find_element_by_xpath("//a[@class='button wc-forward']").click()
        time.sleep(5)
        self.driver.execute_script("window.scrollBy(0,750)", "")
        time.sleep(5)
        self.driver.find_element_by_xpath("//a[@class='checkout-button button alt wc-forward']").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/Users/aarviaditya/Desktop/Testing/HTML_Python"), verbosity=2)


