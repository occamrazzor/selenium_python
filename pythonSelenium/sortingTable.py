from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service('c:/Webdrivers/chromedriver.exe')
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/offers')
browserSortedVeges = []
# Procedure for sorting table
# 1. Click on column header,
driver.find_element(By.XPATH, '//span[text()="Veg/fruit name"]').click()
# 2. Collect all veggie name in a BrowserSortedVege_list[] (B, A, C) in console>$x("//tr/td[1]")
vegeWebElements = driver.find_elements(By.XPATH, '//tr/td[1]')
for vegeElement in vegeWebElements:
    browserSortedVeges.append(vegeElement.text)
originalBrowserSortedList = browserSortedVeges.copy()

# 3. Sort this BrowserSortedVege_list[] to => newSortedVege_list[] -> (A, B, C)
browserSortedVeges.sort()
# 4. BrowserSortedVege_list == newSortedVege_List

assert browserSortedVeges == originalBrowserSortedList
