import datetime
from selenium import webdriver


class Base():

    def __init__(self, driver):
        self.driver = driver



    """Method get current URL (метод URL, на которой находимся)"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current URL: " + get_url)


    """Method screenshot (создание скриншотов)"""

    def get_screenshot(self):
        now_date = datetime.datetime.now().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot('C:\\Users\\Lenovo\\PycharmProjects\\reStoreAuto\\screen\\' + name_screenshot)