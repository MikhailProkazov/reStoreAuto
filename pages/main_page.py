import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Main_page(Base):
    url = 'https://re-store.ru'

    # Locators

    change_region = "//div[@class='header-location__text']"         # вкладка для выбора региона
    region_sochi = "//a[@class='modal-search-region__item'][18]"    # локатор города Сочи
    iphone_tab = "(//div[@class='header-menu__item'])[3]"           # вкладка с айфонами
    cart_button = "(//a[@class='header-icons__link'])[3]"           # корзина
    sale_tab = "(//div[@class='header-menu__item'])[10]"            # вкладка акции, скидки

    # Getters

    def get_change_region(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.change_region)))

    def get_region_sochi(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.region_sochi)))

    def get_iphone_tab(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.iphone_tab)))

    def get_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_button)))

    def get_sale_tab(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sale_tab)))

    # Actions

    def click_change_region(self):
        self.get_change_region().click()
        print("Click change region")

    def click_region_sochi(self):
        self.get_region_sochi().click()
        print("Click select region_sochi")

    def click_iphone_tab(self):
        self.get_iphone_tab().click()
        print("Click iphone tab")

    def click_cart_button(self):
        self.get_cart_button().click()
        print("Click cart button")

    def click_sale_tab(self):
        self.get_sale_tab().click()
        print("Click sale tab")

    # Methods

    def open_cart(self):
        self.get_current_url()
        self.click_cart_button()

    def open_tab_iphone(self):
        self.get_current_url()
        self.click_iphone_tab()
        self.get_current_url()

    def open_tab_sale(self):
        self.get_current_url()
        self.click_sale_tab()
        self.get_current_url()

    def open_url(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    def select_our_region(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(5)
        self.get_current_url()
        self.click_change_region()
        time.sleep(5)
        self.click_region_sochi()
        time.sleep(5)
