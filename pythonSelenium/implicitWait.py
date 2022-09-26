
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


options = Options()
options.add_argument("--disable-web-security")
# chrome_options.add_argument("--disable-site-isolation-trials")
options.add_experimental_option("excludeSwitches", ["enable-logging"])
service_obj = Service("c:/Webdrivers/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=options)
driver.implicitly_wait(5)
driver.get("https://www.rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR,'.search-keyword').send_keys("ber")
#driver.find_element(By.XPATH, "//input[@type='search']").send_keys('ber')
time.sleep(2) # This sleep is required for a list see below.
results = driver.find_elements(By.XPATH, "//div[@class='products']/div") # This generates a list of elements
count = len(results)
print(count)
assert count > 0 
for result in results: #chaining the products to the cart ie chaining parent to child elements...Returns a list[]
    result.find_element(By.XPATH, 'div/button').click()

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
driver.get("https://www.rahulshettyacademy.com/seleniumPractise/#/cart")
#driver.find_element(By.XPATH, "//input[@placeholder='Enter promo code']").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

print(driver.find_element(By.CLASS_NAME, 'promoInfo').text)