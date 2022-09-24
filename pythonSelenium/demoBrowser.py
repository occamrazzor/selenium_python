from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# from selenium.webdriver.firefox.service import Service

# chrome driver is a proxy driver
# Create service object

# Chrome Driver
""" service_obj = Service('C:/Webdrivers/chromedriver.exe')
driver = webdriver.Chrome(service = service_obj) """

# Microsoft Edge Driver
service_obj = Service("C:/Webdrivers/msedgedriver.exe")
driver = webdriver.Edge(service=service_obj)

# Firefox Driver
""" service_obj = Service('C:/Webdrivers/geckodriver.exe')
driver = webdriver.Firefox(service = service_obj) """

driver.maximize_window()
driver.get("https://rahulshettyacademy.com")
print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.back()
driver.refresh()
driver.forward()
driver.close()
