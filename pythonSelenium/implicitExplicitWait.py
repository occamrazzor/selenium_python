import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options_obj = webdriver.ChromeOptions()
options_obj.add_experimental_option("excludeSwitches", ["enable-logging"])

service_obj = Service("c:/Webdrivers/chromedriver.exe")

driver = webdriver.Chrome(service=service_obj, options=options_obj)
driver.get('https://www.rahulshettyacademy.com/seleniumPractise/#/')
driver.find_element(By.CSS_SELECTOR, '.search-keyword').send_keys('berry')
time.sleep(3)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)
assert count > 0 # Assert will pass
for result in results: #chaining the products to the cart ie chaining parent to child elements
    result.find_element(By.XPATH, 'div/button').click()

