from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class  import Base

class Iphone_page(Base):

    # Locators

    iphones_tab = "//span[contains(text(),'iPhone')]"
    filter_iphones_button = "//button[@class='catalog-layout__filter-title']"
    color_iphones_tab = "//div[contains(text(),'Цвет')]"
    green_color_iphone = "//p[contains(text(),'зеленого цвета')]"
    apply_filter_button = "//button[contains(text(),'Применить')]"
    add_item_to_cart = "(//button[@class='product-card__ui-button btn btn--pink btn--size-sm'])[4]"

















