import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.sale_page import Sale_page
from pages.main_page import Main_page

options = webdriver.ChromeOptions()
options.page_load_strategy = 'eager'


def test_add_sale_product_to_cart():
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    print("Start test add sale product to cart")

    mp = Main_page(driver)
    mp.open_url()
    time.sleep(3)
    print("Открылся нужный нам сайт")

    mp.open_sale_tab()
    time.sleep(3)
    print("Открылась вкладка с акциями и спецпредложениями")

    sp = Sale_page(driver)
    sp.add_first_offer_to_cart()
    time.sleep(3)
    print("Выбрали товар и добавили его в корзину через карточку товара")

    mp.open_cart()
    time.sleep(3)
    print("Зашли в корзину")

    print("Finish Test")
