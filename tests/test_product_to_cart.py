import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.main_page import Main_page

options = webdriver.ChromeOptions()
options.page_load_strategy = 'eager'


def test_add_product_to_cart():

