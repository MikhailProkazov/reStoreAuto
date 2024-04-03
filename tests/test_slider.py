from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://re-store.ru/apple-iphone/'
driver.get(base_url)
driver.maximize_window()

filter_tab = driver.find_element(By.XPATH,"//button[@class='catalog-layout__filter-title']")
filter_tab.click()

# actions = ActionChains(driver)
# filter_slide = driver.find_element(By.XPATH,"//div[@class='catalog-layout__sidebar-container scrollbar']")
# actions.click_and_hold(filter_slide).move_by_offset(0,-100).release()