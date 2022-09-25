import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options_obj = webdriver.ChromeOptions()
options_obj.add_experimental_option("excludeSwitches", ["enable-logging"])

service_obj = Service("c:/Webdrivers/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=options_obj)

driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
print(len(checkboxes))
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        break

radioButtons = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
radioButtons[2].click()
assert radioButtons[2].is_selected()

assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert driver.find_element(By.ID, "displayed-text").is_displayed()  # This assertion throws an error
# assert not driver.find_element(By.ID, 'displayed-text').is_displayed() # This assertion will not throws an error
