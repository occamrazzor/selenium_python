from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# To run in headless mode need to add ChromeOptions and include in the driver line 9.
chrome_objects = webdriver.ChromeOptions()
chrome_objects.add_argument('headless')
# To circumvent any SSL certificate errors  use
chrome_objects.add_argument('--ignore-certificate-errors')

service_obj = Service('c:/Webdrivers/chromedriver.exe')
driver = webdriver.Chrome(service=service_obj, options=chrome_objects)
driver.implicitly_wait(5)

driver.get('https://www.rahulshettyacademy.com/AutomationPractice/')
# Injecting Javascript events into selenium python code, use
# execute_script('enter javascript event here find it in console')
#window.scrollBy(0,document.body.scrollHeight) scroll to bottom of the page
driver.execute_script('window.scrollBy(0,document.body.scrollHeight)')
driver.get_screenshot_as_file('screen.png')