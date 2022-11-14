import random
import string
import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from OpenBrowser import OpenBrowser
from Register import Register
from Login import Login
from Search import Search

class TestFullCycle(unittest.TestCase):
    s = Service("D:/Python/chromedriver.exe")
    driver = webdriver.Chrome(service=s)

    def test_1(self):
        open_browser = OpenBrowser(self.driver)
        open_browser.open_webBrowser()

    def test_2(self):
        reg = Register(self.driver)
        reg.registration()
        reg.gender()
        reg.name("Tahsin Adiba", "Nijhum")
        reg.dob(1, "January", 2003)
        reg.email("tahsinnijum@gmail.com")
        reg.company("RedDot Digital")
        reg.password("123456789*")
        reg.Confirmpass("123456789*")
        reg.RegConfirm()
        reg.Logout()

    def test_3(self):
        log = Login(self.driver)
        log.log_in()
        log.log_email("tahsinnijum@gmail.com")
        log.log_password("123456789*")
        log.confirmLog()

    def test_4(self):
        search = Search(self.driver)
        search.searching()
        search.searchproduct("Apple MacBook")



    if __name__ == '__main__':
        unittest.main()
