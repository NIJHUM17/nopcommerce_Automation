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
from Add_To_Cart import Add_To_Cart
from Shopping_cart import Shopping_cart

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
        reg.name("Nilasha", "Nipu")
        reg.dob(1, "January", 2003)
        reg.email("nilasha1111@gmail.com")
        reg.company("RedDot Digital")
        reg.password("00012347899*")
        reg.Confirmpass("00012347899*")
        reg.RegConfirm()
        reg.Logout()

    def test_3(self):
        log = Login(self.driver)
        log.log_in()
        log.log_email("nilasha1111@gmail.com")
        log.log_password("00012347899*")
        log.confirmLog()

    def test_4(self):
        search = Search(self.driver)
        search.searching()
        search.searchproduct("Apple MacBook")
        search.searchinside()

    def test_5(self):
        cart = Add_To_Cart(self.driver)
        cart.add_cart()


    def test_6(self):
        shoppingCart = Shopping_cart(self.driver)
        shoppingCart.Shop_cart()



    if __name__ == '__main__':
        unittest.main()
