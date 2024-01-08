from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
time.sleep(2)
website = 'https://en.wikipedia.org'

driver.get(website)
# driver.maximize_window()
# search_field = driver.find_element(By.NAME, 'search')
# search_field.send_keys('Donald Trump')
# search_field.send_keys(Keys.ENTER)
# welcome_message = driver.find_element(By.CLASS_NAME, 'mw-headline')
# welcome_message = driver.find_element(By.ID, 'Welcome_to_Wikipedia')
# welcome_message = driver.find_element(By.CSS_SELECTOR, 'span.mw-headline')
# print(welcome_message.text)

# wikipedia_link = driver.find_elements(By.TAG_NAME, 'a')
# for link in wikipedia_link:
#     print(link.text)

# wikipedia_link = driver.find_element(By.LINK_TEXT, 'Wikipedia')
# print(wikipedia_link.text)
#
# Shos = driver.find_element(By.PARTIAL_LINK_TEXT, 'Shosta')
# print(Shos.text)
# print(Shos.get_attribute('href'))

# //DIV/HEADER/DIV[1]/NAV[@CLASS='vector-main-menu-landmark']

# featured = driver.find_element(By.XPATH, "//span[@class='mw-headline' and @id=\"From_today's_featured_article\"]")
# print(featured.text)

archive = driver.find_element(By.XPATH, '//*[@id="mp-dyk"]/div[2]/ul/li[1]/b/a')
print(archive.text)