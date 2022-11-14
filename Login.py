import time


class Login:

    def __init__(self, driver):
        self.driver = driver

    def log_in(self):
        time.sleep(2)
        self.driver.find_element("xpath", "//a[@class ='ico-login']").click()
        time.sleep(1)

    def log_email(self, logemail):
        self.driver.find_element("id", "Email").send_keys(logemail)
        time.sleep(1)

    def log_password(self, pass1):
        self.driver.find_element("id", "Password").send_keys(pass1)
        time.sleep(3)

    def confirmLog(self):
        self.driver.find_element("xpath", "//button[@class = 'button-1 login-button']").click()
        time.sleep(3)