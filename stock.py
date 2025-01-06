from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from prettytable import PrettyTable
import time

# Set up Selenium WebDriver 
service = Service('path/to/chromedriver')  #ppdate with your path to chromeDriver
driver = webdriver.Chrome(service=service)

stock_symbols = ['AAPL', 'INTC', 'MSFT', 'NVDA', 'TSLA', 'AMD', 'GOOGL', 'AMZN', 'FB', 'NFLX']
table = PrettyTable()
table.field_names = ['Stock Symbol', 'Stock Price']

for symbol in stock_symbols:
    url = f'https://finance.yahoo.com/quote/{symbol}'
    driver.get(url)
    time.sleep(3)  # waiting for JS to load

    try:
        price_element = driver.find_element(By.XPATH, '//fin-streamer[@data-field="regularMarketPrice"]')
        stock_price = price_element.text
    except Exception as e:
        stock_price = None

    table.add_row([symbol, stock_price])

driver.quit()
print(table)
