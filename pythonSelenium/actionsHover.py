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
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
action = ActionChains(driver)
#action.double_click(driver.find_element(By.))
#action.drag_and_drop()
# Note for action you need to postfix with perform method
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
# Note context_click is a right click action on the element
#action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()