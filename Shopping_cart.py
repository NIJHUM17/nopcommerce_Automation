import time

class Shopping_cart:

    def __init__(self, driver):
        self.driver = driver

    def Shop_cart(self):
        time.sleep(3)
        self.driver.find_element("xpath", "//span[@class = 'cart-label']").click()
        time.sleep(1)
