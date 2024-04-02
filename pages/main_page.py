import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Main_page(Base):

    url = 'https://re-store.ru'


    # Locators

    change_region = "//div[@class='header-location__text']"
    region_sochi = "//a[@class='modal-search-region__item'][18]"


    # Getters

    def get_change_region(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.change_region)))

    def get_region_sochi(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.region_sochi)))


    # Actions

    def click_change_region(self):
        self.get_change_region().click()
        print("Click change region")

    def click_region_sochi(self):
        self.get_region_sochi().click()
        print("Click select region_sochi")


    # Methods

    def select_our_region(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(5)
        self.get_current_url()
        self.click_change_region()
        time.sleep(5)
        self.click_region_sochi()
        time.sleep(5)



