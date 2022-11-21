
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


from pageObject.OpenBrowser import OpenBrowser
from pageObject.Register import Register
from pageObject.Login import Login
from pageObject.Search import Search
from pageObject.Shopping_cart import Shopping_cart
from pageObject.Checkout import Checkout

class TestFullCycle(unittest.TestCase):
    s = Service("D:/Python/nopcommerceAutomation/Driver/chromedriver.exe")
    driver = webdriver.Chrome(service=s)

    def test_1(self):
        open_browser = OpenBrowser(self.driver)
        open_browser.open_webBrowser()

    def test_2(self):
        reg = Register(self.driver)
        reg.registration()
        reg.gender()
        reg.name()
        reg.dob()
        reg.email()
        reg.company()
        reg.password()
        reg.Confirmpass()
        reg.RegConfirm()
        reg.Logout()

    def test_3(self):
        log = Login(self.driver)
        log.log_in()
        log.log_email()
        log.log_password()
        log.confirmLog()

    def test_4(self):
        search = Search(self.driver)
        search.searching()
        search.searchproduct()
        search.searchinside()

    def test_5(self):
        cart = Shopping_cart(self.driver)
        cart.add_cart()
        cart.Shop_cart()

    def test_6(self):
        checkout = Checkout(self.driver)
        checkout.checkout_button()
        checkout.billing_address()
        checkout.continue_button()


    if __name__ == '__main__':
        unittest.main()
