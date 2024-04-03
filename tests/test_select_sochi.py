import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.main_page import Main_page

options = webdriver.ChromeOptions()
options.page_load_strategy = 'eager'


def test_select_region_sochi():
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))


    print("Start test for select our region Sochi")

    mp = Main_page(driver)
    mp.select_our_region()

    time.sleep(5)

    print("Finish test for select our region Sochi")