import random
import string
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class OpenBrowser:

    def __init__(self, driver):
        self.driver = driver

    def open_webBrowser(self):
        self.driver.get("https://demo.nopcommerce.com/")
        self.driver.maximize_window()
        print(self.driver.title)
        time.sleep(3)

