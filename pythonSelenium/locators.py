from selenium import webdriver
from selenium.webdriver.common.by import By

#Chrome Driver
from selenium.webdriver.chrome.service import Service

service_obj = Service('C:/Drivers/geckodriver.exe')
driver = webdriver.Firefox(service= service_obj)

driver.get('https://rahulshettyacademy.com/angularpractice/')

#ID, Xpath, CSSSelector, Classname, name, linkText
driver.find_element(By.NAME, 'email').send_keys('tester@test.com')
driver.find_element(By.ID, 'exampleInputPassword1').send_keys('tester')
driver.find_element(By.ID, 'exampleCheck1').click()

# XPath.........//tagname[@attribute='value']
# //input[@type='submit']
driver.find_element(By.XPATH, "//input[@type='submit']" ).click()

# By.CLASS_NAME
message = driver.find_element(By.CLASS_NAME, 'alert-success').text
print(message)
assert "Success" in message

# By.CSS_Selector........."tagname[attribute='value']"...//input[@type='submit'].....#id  .classname ...valid CSS
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys('occamRazor')

driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys('OCCAMRAZOR')
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()