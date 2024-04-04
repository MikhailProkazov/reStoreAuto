import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.iphone_page import Iphone_page
from pages.main_page import Main_page

options = webdriver.ChromeOptions()
options.page_load_strategy = 'eager'




def test_add_product_to_cart():
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    print("Start test filter and select product to cart")

    mp = Main_page(driver)
    mp.open_url()
    time.sleep(3)
    print("Открылся нужный нам сайт")

    mp.open_tab_iphone()
    time.sleep(3)
    print("Открылась вкладка с айфонами")

    ipp = Iphone_page(driver)
    ipp.filter_and_select_product_to_cart()

    print("Finish Test")






