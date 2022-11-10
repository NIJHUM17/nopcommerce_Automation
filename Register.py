import random
import string
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class Register:

    def __init__(self, driver):
        self.driver = driver

    def Reg(self):
        self.driver.find_element("xpath", "//a[@class = 'ico-register']").click()

    def Gender(self):
        self.driver.find_element("xpath", "//input[@id='gender-female']").click()

    def name(self, firstname, lastname):
        self.driver.find_element("id", "FirstName").send_keys(firstname)
        self.driver.find_element("id", "LastName").send_keys(lastname)

    def dob(self, day, month, year):
        self.driver.find_element("name", "DateOfBirthDay").send_keys(day)
        self.driver.find_element("name", "DateOfBirthMonth").send_keys(month)
        self.driver.find_element("name", "DateOfBirthYear").send_keys(year)
        time.sleep(2)

    def email(self, myemail):
        self.driver.find_element("id", "Email").send_keys(myemail)
        time.sleep(2)
    def company(self, mycompany):
        self.driver.find_element("id", "Company").send_keys(mycompany)
        time.sleep(1)

    def password(self, pass1):
        self.driver.find_element("id", "Password").send_keys(pass1)
        time.sleep(1)

    def Confirmpass(self, pass1):
        self.driver.find_element("id", "ConfirmPassword").send_keys(pass1)
        time.sleep(1)

    def RegConfirm(self):
        self.driver.find_element("xpath", "//button[@class= 'button-1 register-next-step-button']").click()




