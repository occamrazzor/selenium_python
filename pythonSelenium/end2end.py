from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service('C:/Webdrivers/chromedriver.exe')
driver = webdriver.Chrome(service = service_obj)

# XPATH -> '//a[contains(@href,"shop")]' Note: with regular expression
# CSS -> a[href*='shop'] Note: with regular expression
driver.get('https://www.rahulshettyacademy.com/angularpractice/')
driver.find_element(By.XPATH, '//a[contains(@href,"shop")]').click()

products = driver.find_elements(By.XPATH, '//div[@class="card h-100"]')

for product in products:


