import time

class Add_To_Cart:

    def __init__(self, driver):
        self.driver = driver

    def add_cart(self):
        time.sleep(4)
        self.driver.find_element("xpath", "//button[@class ='button-1 add-to-cart-button']").click()
        time.sleep(1)





