from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class  import Base

class Cart_page(Base):


    # Locators

    cart_button = "(//a[@class='header-icons__link'])[3]"

