from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base



class Sale_page(Base):


    # Locators

    first_offer = "(//div[@class='catalog__product product-card product-card--hovered'])[1]"
    card_first_offer_add_to_cart = "//button[@class='btn btn--pink btn--full-width btn--animated']"


    # Getters

    def get_first_offer(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_offer)))

    def get_card_first_offer_add_to_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.card_first_offer_add_to_cart)))


    # Actions

    def click_first_offer(self):
        self.get_first_offer().click()
        print("Click first offer")

    def click_card_first_offer_add_to_cart(self):
        self.get_card_first_offer_add_to_cart().click()
        print("Click mac 15 add to cart")


    # Methods

    def add_first_offer_to_cart(self):
        self.click_first_offer()                                # вибираем товар
        self.click_card_first_offer_add_to_cart()               # добавляем товар в корзину
        print("Добавили товар в корзину")




