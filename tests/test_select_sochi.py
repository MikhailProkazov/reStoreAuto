import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.main_page import Main_page

options = webdriver.ChromeOptions()
options.page_load_strategy = 'eager'

@pytest.mark.run(order=3)
def test_select_region_sochi():
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    time.sleep(5)

    print("Start test for select our region")

    mp = Main_page(driver)
    mp.select_our_region()

    time.sleep(5)

    print("Finish test")