import datetime
from selenium import webdriver


class Base():

    def __init__(self, driver):
        self.driver = driver

    """Method get current URL (метод URL, на которой находимся)"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current URL: " + get_url)