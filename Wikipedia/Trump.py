from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os
import requests
import wget

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")

driver = webdriver.Chrome(options=options)
website = 'https://en.wikipedia.org'

driver.get(website)
search_field = driver.find_element(By.NAME, 'search')
search_field.send_keys('Donald Trump')
search_field.send_keys(Keys.ENTER)

title = driver.find_element(By.CLASS_NAME, 'mw-page-title-main')


images_directory = f'{title.text} Images'
audios_directory = f'{title.text} Audios'
os.makedirs(images_directory, exist_ok=True)
os.makedirs(audios_directory, exist_ok=True)

sections = []
sections_elements = driver.find_elements(By.XPATH, '//li/a[@class="vector-toc-link"]/div[@class="vector-toc-text"]')

for section_element in sections_elements:
    section_name = section_element.text

    if section_name:
        sections.append(section_name)



last_section_name = sections[-1]

last_span_xpath = f"//span[@class='mw-headline' and contains(text(), '{last_section_name}')]"
last_section = driver.find_element(By.XPATH, last_span_xpath)
last_preceding_paragraphs = last_section.find_elements(By.XPATH,
                                                       "./preceding::p | ./preceding::h3/span[@class='mw-headline'] | "
                                                       "./preceding::h2/span[@class='mw-headline']")

text_filename = 'All about Donald Trump.txt'

with open(text_filename, 'w', encoding='utf-8') as txt_file:
    for preceding_paragraph in last_preceding_paragraphs:

        if preceding_paragraph.tag_name == 'span':
            txt_file.write('-----------------------------\n')
        txt_file.write(preceding_paragraph.text + '\n')


images = driver.find_elements(By.XPATH, '//img[contains(@alt, "Trump")]')

for index, image in enumerate(images):
    image_url = image.get_attribute('src')
    response = requests.get(image_url, stream=True)

    if response.status_code == 200:
        image_filename = f'{images_directory}/image_{index + 1}.jpg'
        with open(image_filename, 'wb') as img_file:
            for chunk in response.iter_content(chunk_size=8192):
                img_file.write(chunk)

play_button = driver.find_element(By.XPATH, '//a[@class="mw-tmh-play"]')
play_button.click()
time.sleep(1)
audio = driver.find_element(By.XPATH, '//audio/source')
audio_url = audio.get_attribute('src')
wget.download(audio_url, f'{audios_directory}/audio.mp3')