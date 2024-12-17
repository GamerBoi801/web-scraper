from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

# Set up Selenium (make sure you have ChromeDriver installed)
driver = webdriver.Chrome()  # or use another browser driver

# URL for the target Nike products page (replace with an actual URL)
url = 'https://www.nike.com/cn'
driver.get(url)

# Get page source after JavaScript has rendered it
html = driver.page_source

# Parse with BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Find all product containers (adjust class name based on actual HTML structure)
products = soup.find_all('div', class_="product")  # Adjust this based on actual class names

# Extracting product names and prices as before...

# Close the driver after scraping
driver.quit()
