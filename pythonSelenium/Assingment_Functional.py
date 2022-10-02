from gettext import find
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
expectedList = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
actualList = []

options = Options()
options.add_argument("--disable-web-security")
# chrome_options.add_argument("--disable-site-isolation-trials")
options.add_experimental_option("excludeSwitches", ["enable-logging"])
service_obj = Service("c:/Webdrivers/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=options)
driver.implicitly_wait(2) # This timeout is applied globally and wait will be over the moment the element appear.
driver.get("https://www.rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR,'.search-keyword').send_keys("ber")
time.sleep(4)

results = driver.find_elements(By.XPATH, "//div[@class='products']/div") # This generates a list of elements
count = len(results)
print(count)
assert count > 0 
for result in results: #chaining the products  ie chaining parent to child elements...Returns a list[]
    actualList.append(result.find_element(By.CSS_SELECTOR, "h4.product-name").text)
    #result.find_element(By.XPATH, "div/button").click()
print(actualList)
print(expectedList)
assert expectedList == actualList

#############################################
for result in results: #chaining the products to the cart ie chaining parent to child elements...Returns a list[]
    result.find_element(By.XPATH, 'div/button').click()

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
driver.get("https://www.rahulshettyacademy.com/seleniumPractise/#/cart")
#driver.find_element(By.XPATH, "//input[@placeholder='Enter promo code']").send_keys("rahulshettyacademy")

# Sum Validation

prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sum = 0
for price in prices:
    sum = sum + int(price.text)

print(sum)
totalAmount =int((driver.find_element(By.CSS_SELECTOR,".totAmt").text))

assert sum == totalAmount

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
print(driver.find_element(By.CLASS_NAME, 'promoInfo').text)

discountedAmount = float(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)
print (float(discountedAmount))
assert totalAmount > discountedAmount