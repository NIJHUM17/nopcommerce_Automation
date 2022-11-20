import time

class Checkout:

    def __init__(self, driver):
        self.driver = driver

    def add_cart(self):
        time.sleep(4)
        self.driver.find_element("xpath", "//button[@class ='button-1 add-to-cart-button']").click()
        time.sleep(1)

    def Shop_cart(self):
        time.sleep(3)
        self.driver.find_element("xpath", "//span[@class = 'cart-label']").click()
        time.sleep(1)





