from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import os

# Initialize WebDriver
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
# options.add_argument('--headless')  # Uncomment for headless mode
driver = webdriver.Chrome(service=service, options=options)

# Base URLs for electric and acoustic guitars
base_urls = {
    'electric_guitars': 'https://reverb.com/marketplace?query=guitar&condition=used&country_of_origin=US&product_type=electric-guitars&category=solid-body&page=',
    'acoustic_guitars': 'https://reverb.com/marketplace?query=guitar&condition=used&country_of_origin=US&product_type=acoustic-guitars&category=dreadnought&page='
}

# Create subdirectories for HTML files if they don't exist
directories = ['./electric_guitars_html/', './acoustic_guitars_html/']
for directory in directories:
    if not os.path.exists(directory):
        os.makedirs(directory)

for guitar_type, base_url in base_urls.items():
    dir_path = f"./{guitar_type}_html/"  # Determine the directory path based on guitar type
    for page in range(1, 41):  # Looping through pages 1 to 41
        url = f"{base_url}{page}"
        driver.get(url)

        time.sleep(10)  # wait 10 seconds

        # Retrieve and format the page HTML
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        formatted_html = soup.prettify()

        # Construct the file name and path
        filepath = os.path.join(dir_path, f'{guitar_type}_page_{page}.html')
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(formatted_html)

# Quit the WebDriver
driver.quit()
