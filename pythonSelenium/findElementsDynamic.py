import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options_obj = webdriver.ChromeOptions()
options_obj.add_experimental_option("excludeSwitches", ["enable-logging"])

service_obj = Service("c:/Webdrivers/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=options_obj)

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)

# Scan the list and then choose the target country using css locator (tagname[attribute="value")
# To retrieve the country name .text method will not work. ie print(driver.find_element(By.ID, 'autosuggest').text) but use .get_Attribute

countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print(len(countries))
for country in countries:
    if country.text == "India":
        country.click()
        break

print(driver.find_element(By.ID, 'autosuggest').get_attribute('value'))
assert (driver.find_element(By.ID, 'autosuggest').get_attribute('value')) == 'India'