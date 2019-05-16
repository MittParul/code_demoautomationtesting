import time
from selenium.webdriver.support.ui import Select
class Register():

    def __init__(self,driver):

        self.driver = driver
        self.driver.firstname_xpath = "//input[@placeholder='First Name']"
        self.driver.lastname_xpath = "//input[@placeholder='Last Name']"
        self.driver.address_xpath = "/html[1]/body[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[2]/div[1]/textarea[1]"
        self.driver.email_xpath = "/html[1]/body[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[3]/div[1]/input[1]"
        self.driver.phone_xpath = "/html[1]/body[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[4]/div[1]/input[1]"
        self.driver.gender_click_xpath = "//label[1]//input[1]"
        self.driver.hobbies_click_xpath = "//input[@id='checkbox2']"
        self.driver.language_click_xpath = "//div[@id='msdd']"
        self.driver.English_click_xpath = "//a[contains(text(),'English')]"
        self.driver.skills_click_xpath = "//select[@id='Skills']"
        self.driver.country_click_xpath = "// select[ @ id = 'countries']"
        self.driver.year_click_xpath = "// select[ @ id = 'yearbox']"
        self.driver.month_click_xpath = "//select[@placeholder='Month']"
        self.driver.day_click_xpath = "//select[@id='daybox']"
        self.driver.password_click_xpath = "//input[@id='firstpassword']"
        self.driver.confirm_click_xpath = "//input[@id='secondpassword']"
        self.driver.submit_click_xpath = "//button[@id='submitbtn']"


    def text_name(self,firstname):
        self.driver.find_element_by_xpath(self.driver.firstname_xpath).send_keys(firstname)


    def text_lastname(self,lastname):
        self.driver.find_element_by_xpath(self.driver.lastname_xpath).send_keys(lastname)
        time.sleep(5)

    def text_address(self,address,email,phone):
        self.driver.find_element_by_xpath(self.driver.address_xpath).send_keys(address)
        self.driver.find_element_by_xpath(self.driver.email_xpath).send_keys(email)
        self.driver.find_element_by_xpath(self.driver.phone_xpath).send_keys(phone)
        time.sleep(5)

    def click_gender_hobbies(self):
        self.driver.find_element_by_xpath(self.driver.gender_click_xpath).click()
        self.driver.find_element_by_xpath(self.driver.hobbies_click_xpath).click()
        time.sleep(5)

    def text_language(self):
        self.driver.find_element_by_xpath( self.driver.language_click_xpath).click()
        self.driver.find_element_by_xpath(self.driver.English_click_xpath).click()
        time.sleep(5)

    def link_skills(self):
        skills = self.driver.find_element_by_xpath(self.driver.skills_click_xpath)
        drp = Select(skills)
        drp.select_by_visible_text("Analytics")
        self.driver.implicitly_wait(10)
        time.sleep(5)

    def link_country(self):
        country = self.driver.find_element_by_xpath(self.driver.country_click_xpath)
        drp1 = Select(country)
        drp1.select_by_visible_text("Australia")
        self.driver.implicitly_wait(10)

    def link_date(self):
        year = self.driver.find_element_by_xpath(self.driver.year_click_xpath)
        drp2 = Select(year)
        drp2.select_by_visible_text("1982")
        self.driver.implicitly_wait(10)
        month = self.driver.find_element_by_xpath(self.driver.month_click_xpath)
        drp3 = Select(month)
        drp3.select_by_visible_text("January")
        self.driver.implicitly_wait(10)
        day = self.driver.find_element_by_xpath(self.driver.day_click_xpath)
        drp4 = Select(day)
        drp4.select_by_visible_text("18")
        self.driver.implicitly_wait(10)

    def text_password(self,password,confirm):
        self.driver.find_element_by_xpath(self.driver.password_click_xpath).send_keys(password)
        self.driver.find_element_by_xpath(self.driver.confirm_click_xpath).send_keys(confirm)
        time.sleep(5)

    def click_submit(self):
        self.driver.find_element_by_xpath(self.driver.submit_click_xpath).click()
        time.sleep(5)
