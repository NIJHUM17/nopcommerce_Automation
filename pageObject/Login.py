import time

import testData.registrationData
import testData.loginData


class Login:

    def __init__(self, driver):
        self.driver = driver

    def log_in(self):
        time.sleep(2)
        self.driver.find_element("xpath", "//a[@class ='ico-login']").click()
        time.sleep(1)

    def log_email(self):
        self.driver.find_element("id", "Email").send_keys(testData.loginData.logemail)
        time.sleep(1)

    def log_password(self):
        self.driver.find_element("id", "Password").send_keys(testData.loginData.logpass)
        time.sleep(3)

    def confirmLog(self):
        self.driver.find_element("xpath", "//button[@class = 'button-1 login-button']").click()
        time.sleep(3)
