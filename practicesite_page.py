import time

class practice():

    def __init__(self,driver):

        self.driver = driver
        self.click_practice_xpath = "// a[contains(text(), 'Practice Site')]"
        self.click_product_xpath = "// h3[contains(text(), 'Thinking in HTML')]"
        self.click_add_to_cart_xpath = "// button[@class ='single_add_to_cart_button button alt']"
        self.click_view_cart_xpath = "//a[@class='button wc-forward']"
        self.click_proceed_checkout_xpath = "//a[@class='checkout-button button alt wc-forward']"

    def click_practice(self):
        self.driver.find_element_by_xpath(self.click_practice_xpath).click()
        time.sleep(5)
        self.driver.execute_script("window.scrollBy(0,750)", "")
        time.sleep(5)

    def click_product(self):
        self.driver.find_element_by_xpath(self.click_product_xpath).click()
        self.driver.find_element_by_xpath(self.click_add_to_cart_xpath).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.click_view_cart_xpath).click()
        self.driver.execute_script("window.scrollBy(0,750)", "")
        time.sleep(5)
        self.driver.find_element_by_xpath(self.click_proceed_checkout_xpath).click()




