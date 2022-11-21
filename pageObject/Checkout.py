import time

class Checkout:

    def __init__(self, driver):
        self.driver = driver


    def terms_of_service(self):
        time.sleep(4)
        self.driver.find_element