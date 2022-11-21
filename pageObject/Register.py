
import time

import testData.registrationData


class Register:

    def __init__(self, driver):
        self.driver = driver

    def registration(self):
        time.sleep(2)
        self.driver.find_element("xpath", "//a[@class = 'ico-register']").click()

    def gender(self):
        self.driver.find_element("xpath", "//input[@id='gender-female']").click()

    def name(self):
        self.driver.find_element("id", "FirstName").send_keys(testData.registrationData.firstname)
        self.driver.find_element("id", "LastName").send_keys(testData.registrationData.lastname)

    def dob(self):
        self.driver.find_element("name", "DateOfBirthDay").send_keys(testData.registrationData.day)
        self.driver.find_element("name", "DateOfBirthMonth").send_keys(testData.registrationData.month)
        self.driver.find_element("name", "DateOfBirthYear").send_keys(testData.registrationData.year)
        time.sleep(2)

    def email(self):
        self.driver.find_element("id", "Email").send_keys(testData.registrationData.myemail)
        time.sleep(2)
    def company(self):
        self.driver.find_element("id", "Company").send_keys(testData.registrationData.mycompany)
        time.sleep(1)


    def password(self):
        self.driver.find_element("id", "Password").send_keys(testData.registrationData.mypass)
        time.sleep(1)

    def Confirmpass(self):
        self.driver.find_element("id", "ConfirmPassword").send_keys(testData.registrationData.mypass)
        time.sleep(1)

    def RegConfirm(self):
        self.driver.find_element("xpath", "//button[@class= 'button-1 register-next-step-button']").click()
        time.sleep(2)

    def Logout(self):
        time.sleep(5)
        self.driver.find_element("xpath", "//a[@class= 'ico-logout']").click()
        time.sleep(1)


