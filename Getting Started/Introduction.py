from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time


path = 'F:/Programming/Udemy/Python Selenium/drivers/chromedriver.exe'
service = Service(executable_path=path)
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(service=service, options=options)

# driver.implicitly_wait(3)
time.sleep(2)
driver.get('https://www.google.com/')

# input('Press any button to close the browser')
