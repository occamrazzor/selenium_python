""" Switch to Alert Example, enter name and click Alert and popup should appear with message and then click the ok button. """
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
name = 'occam'
driver.find_element(By.CSS_SELECTOR, '#name').send_keys(name)
driver.find_element(By.ID, 'alertbtn').click()
# Need to switch from driver mode to alert mode
alert = driver.switch_to.alert
alertText = alert.text
print(alertText)
assert name in alertText
time.sleep(2)
alert.accept()
