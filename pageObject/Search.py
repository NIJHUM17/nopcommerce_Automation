import time
import testData.searchData

class Search:

    def __init__(self, driver):
        self.driver = driver

    def searching(self):
        time.sleep(3)
        self.driver.find_element("xpath", "//input[@class ='search-box-text ui-autocomplete-input']").click()
        time.sleep(3)

    def searchproduct(self):
        self.driver.find_element("id","small-searchterms").send_keys(testData.searchData.productName)
        time.sleep(1)

    def searchinside(self):
        self.driver.find_element("xpath", "//a[@href = '/apple-macbook-pro-13-inch']").click()
        time.sleep(3)



