from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options 

options_obj = webdriver.ChromeOptions()
options_obj.add_experimental_option("excludeSwitches", ["enable-logging"])
# driver = webdriver.Chrome(options=options) """


# XPath- //tagname[@attribute = 'value']......//input[@type='submit']
service_obj = Service('c:/Webdrivers/chromedriver.exe')
driver = webdriver.Chrome(service=service_obj, options=options_obj)
driver.get('https:/rahulshettyacademy.com/client')
#driver.find_element(By.LINK_TEXT, 'Forgot password?').click()
driver.find_element(By.PARTIAL_LINK_TEXT, 'password?').click()
driver.find_element(By.XPATH, '//form/div[1]/input' ).send_keys('demo@gmail.com')
driver.find_element(By.XPATH, '//form/div[2]/input').send_keys('occam')
driver.find_element(By.CSS_SELECTOR, 'form div:nth-child(3) input').send_keys('occam')
#driver.find_element(By.CSS_SELECTOR, '#confirmPassword').send_keys('occam')
#driver.find_element(By.XPATH, "//button[@type='submit']").click()
driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()