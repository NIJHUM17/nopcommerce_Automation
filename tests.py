import random
import string
import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from OpenBrowser import OpenBrowser
from Register import Register


class TestFullCycle(unittest.TestCase):
    s = Service("D:/Python/chromedriver.exe")
    driver = webdriver.Chrome(service=s)

    def test_setup(self):
        open_browser = OpenBrowser(self.driver)
        open_browser.open_webBrowser()

    def test_1(self):
        reg = Register(self.driver)
        reg.Reg()
        reg.Gender()
        reg.name("Tahsin Adiba", "Nijhum")
        reg.dob(5,"January", 2000)
        reg.email("tahsinanijum5199@gmail.com")
        reg.company("RedDot Digital")
        reg.password("123Nipu*")
        reg.Confirmpass("123Nipu*")
        reg.RegConfirm()

    if __name__ == '__main__':
        unittest.main()