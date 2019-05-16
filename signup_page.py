class signup():

    def __init__(self,driver):

        self.driver = driver
        self.driver.signup_link_xpath = "//img[@id='enterimg']"

    def click_signup(self):
        self.driver.find_element_by_xpath(self.driver.signup_link_xpath).click()