from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service('C:/Webdrivers/chromedriver.exe')
driver = webdriver.Chrome(service=service_obj)

# XPATH -> '//a[contains(@href,"shop")]' Note: with regular expression
# CSS -> a[href*='shop'] Note: with regular expression
driver.implicitly_wait(4)
driver.get('https://www.rahulshettyacademy.com/angularpractice/')
# Note if the window is not maximised then test fails
driver.maximize_window()
driver.find_element(By.XPATH, '//a[contains(@href,"shop")]').click()

products = driver.find_elements(By.XPATH, '//div[@class="card h-100"]')
# Note: There is no driver.find elements because its in a loop and uses product index to locate element
for product in products:
    productName = product.find_element(By.XPATH, 'div/h4/a').text
    if productName == 'Blackberry':
        product.find_element(By.XPATH, 'div/button').click()

driver.find_element(By.CSS_SELECTOR, 'a[class*="btn-primary"]').click()
driver.find_element(By.XPATH, '//button[@class="btn btn-success"]').click()
driver.find_element(By.ID, 'country').send_keys('ind')
wait = WebDriverWait(driver, 10)

# Note: The By.LINK_TEXT, 'India' locator needs to be in its own bracket
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, 'India')))
driver.find_element(By.LINK_TEXT, 'India').click()
driver.find_element(By.XPATH, '//div[@class="checkbox checkbox-primary"]').click()
driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
successText = driver.find_element(By.CLASS_NAME,'alert-success').text
# Use in for partial text comparison
assert 'Success! Thank you!' in successText
driver.close()
