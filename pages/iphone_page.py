import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base



class Iphone_page(Base):


    # Locators

    select_iphone_15_pro_max_256 = "(//div[@class='catalog__product product-card product-card--hovered'])[2]"   # нужный нам товар
    select_product_to_favorite = "//div[@class='favorite has-tooltip']"                                         # добавить товар в избранное
    tab_favorite = "(//div[@class='header-dropdown'])[2]"                                                       # вкладка избранное


    # Getters


    def get_select_iphone_15_pro_max_256(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.select_iphone_15_pro_max_256)))

    def get_select_product_to_favorite(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.select_product_to_favorite)))

    def get_tab_favorite(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.tab_favorite)))




    # Actions



    def click_select_iphone_15_pro_max_256(self):
        self.get_select_iphone_15_pro_max_256().click()
        print("Click select iphone 15 pro max 256")

    def click_select_product_to_favorite(self):
        self.get_select_product_to_favorite().click()
        print("Click select product to favorite")

    def click_tab_favorite(self):
        self.get_tab_favorite().click()
        print("Click tab favorite")



    # Methods

    def filter_and_select_product_to_cart(self):
        self.get_current_url()                      # проверка корректности url
        self.click_select_iphone_15_pro_max_256()   # выбираем нужный нам товар
        print("Выбрали нужный нам товар")
        # time.sleep(3)
        self.get_current_url()                      # проверка корректности url
        self.click_select_product_to_favorite()     # добавляем товар в избранное
        print("Добавили товар в избранное")
        # time.sleep(3)
        self.click_tab_favorite()                   # открываем вкладку избранное
        self.get_current_url()                      # проверка корректности url





























