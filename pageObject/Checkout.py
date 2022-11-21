import time
import testData.registrationData
import testData.checkoutData

class Checkout:

    def __init__(self, driver):
        self.driver = driver


    def checkout_button(self):
        time.sleep(4)
        self.driver.find_element("xpath", "//input[@id='termsofservice']").click()
        self.driver.find_element("xpath", "//button[@id= 'checkout']").click()
        time.sleep(1)
    def billing_address(self):
        self.driver.find_element("id", "BillingNewAddress_CountryId").send_keys(testData.checkoutData.country)
        time.sleep(2)
        self.driver.find_element("id", "BillingNewAddress_City").send_keys(testData.checkoutData.city)
        time.sleep(1)
        self.driver.find_element("id", "BillingNewAddress_Address1").send_keys(testData.checkoutData.address1)
        self.driver.find_element("id", "BillingNewAddress_Address2").send_keys(testData.checkoutData.address2)
        time.sleep(1)
        self.driver.find_element("id", "BillingNewAddress_ZipPostalCode").send_keys(testData.checkoutData.zip_code)
        self.driver.find_element("id", "BillingNewAddress_PhoneNumber").send_keys(testData.checkoutData.phone_no)
        self.driver.find_element("id", "BillingNewAddress_FaxNumber").send_keys(testData.checkoutData.fax_no)
        time.sleep(1)
    def continue_button(self):
        self.driver.find_element("xpath", "//button[@class = 'button-1 new-address-next-step-button']").click()
        time.sleep(3)
        self.driver.find_element("xpath", "//button[@class = 'button-1 shipping-method-next-step-button']").click()
        time.sleep(1)
        self.driver.find_element("xpath", "//button[@class = 'button-1 payment-method-next-step-button']").click()
        self.driver.find_element("xpath", "//button[@class = 'button-1 payment-info-next-step-button']").click()
        self.driver.find_element("xpath", "//button[@class = 'button-1 confirm-order-next-step-button']").click()

        time.sleep(4)
        self.driver.close()



