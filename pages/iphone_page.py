import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base



class Iphone_page(Base):


    # Locators

    filter_iphone_button = "//button[@class='catalog-layout__filter-title']"                 # развернуть вкладку фильтры
    color_iphone_tab = "//div[contains(text(),'Цвет')]"                                      # развернуть вкладку цвета для выбора
    green_color_iphone = "//p[contains(text(),'зеленого цвета')]"                            # выбрать зеленый цвет
    apply_filter_button = "//button[contains(text(),'Применить')]"                           # нажать кнопку "применить"
    add_item_to_cart = "(//div[@class ='product-card__bottom'])[4]"                          # добавить товар в корзину


    # Getters

    def get_filter_iphone_button(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.filter_iphone_button)))

    def get_color_iphone_tab(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.color_iphone_tab)))

    def get_green_color_iphone(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.green_color_iphone)))

    def get_apply_filter_button(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.apply_filter_button)))

    def get_add_item_to_cart(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.add_item_to_cart)))

    # Actions

    def click_filter_iphone_button(self):
        self.get_filter_iphone_button().click()
        print("Click filter iphone button")

    def click_color_iphone_tab(self):
        self.get_color_iphone_tab().click()
        print("Click color iphone tab")

    def click_green_color_iphone(self):
        self.get_green_color_iphone().click()
        print("Click green color iphone")

    def click_apply_filter_button(self):
        self.get_apply_filter_button().click()
        print("Click apply filter button")

    def click_add_item_to_cart(self):
        self.get_add_item_to_cart().click()
        print("Click add item to cart")


    # Methods

    def filter_and_select_product_to_cart(self):
        self.get_current_url()
        self.click_filter_iphone_button()   # нажимаем на вкладку фильтр
        time.sleep(5)
        self.click_color_iphone_tab()       # нажимаем на вкладку цвета
        time.sleep(5)
        self.click_green_color_iphone()     # выбираем зеленый цвет
        time.sleep(5)
        # self.click_apply_filter_button()    # нажимаем на кнопку применить
        # time.sleep(5)
        # self.get_current_url()
        # self.click_add_item_to_cart()       # добавляем товар в корзину


























