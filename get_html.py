from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

# WebDriver
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
# options.add_argument('--headless')
driver = webdriver.Chrome(service=service, options=options)

url = 'https://reverb.com/marketplace?query=guitar&product_type=electric-guitars&condition=used'
driver.get(url)

time.sleep(10)  # wait 10 second

# get html
html = driver.page_source

# using BeautifulSoup format HTML
soup = BeautifulSoup(html, 'html.parser')
formatted_html = soup.prettify()

filepath = 'C:\\Users\\DELL\\Desktop\\code\\Deeplearning\\Image-Based-Price-Estimation\\page.html'
# save.html file
with open('page.html', 'w', encoding='utf-8') as file:
    file.write(formatted_html)

# quit WebDriver
driver.quit()
