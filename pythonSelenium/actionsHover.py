import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
# Expected list ['Cucumber - 1kg', 'Raspberry' - 1/4 kg', 'Strawberry - 1/4 kg']

options = Options()
options.add_argument("--disable-web-security")
# chrome_options.add_argument("--disable-site-isolation-trials")
options.add_experimental_option("excludeSwitches", ["enable-logging"])
service_obj = Service("c:/Webdrivers/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=options)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
action = ActionChains(driver)
action.double_click(driver.find_element(By.))
action.context_click()
action.drag_and_drop()
action.move_to_element()
