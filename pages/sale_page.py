import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base



class Sale_page(Base):


    # Locators

    marshall_stanmore = "(//div[@class='catalog__product product-card product-card--hovered'])[2]"
    marshall_stanmore_add_to_cart = "//button[@class='btn btn--pink btn--full-width btn--animated']"


    # Getters

    def get_marshall_stanmore(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.marshall_stanmore)))

    def get_marshall_stanmore_add_to_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.marshall_stanmore_add_to_cart)))


    # Actions

    def click_marshall_stanmore(self):
        self.get_marshall_stanmore().click()
        print("Click marshall stanmore")

    def click_marshall_stanmore_add_to_cart(self):
        self.get_marshall_stanmore_add_to_cart().click()
        print("Click tmarshall stanmore add to cart")


    # Methods

    def select_marshall_to_cart(self):
        self.get_current_url()
        self.get_marshall_stanmore()                # вибираем товар
        self.get_marshall_stanmore_add_to_cart()    # добавляем товар в корзину
        print("Добавили товар в корзину")




