import time

class Search:

    def __init__(self, driver):
        self.driver = driver

    def searching(self):
        self.driver.find_element("xpath", "//input[@class ='search-box-text ui-autocomplete-input']").click()
        time.sleep(3)

    def searchproduct(self, productName):
        self.driver.find_element("id","small-searchterms").send_keys(productName)
        time.sleep(1)

    