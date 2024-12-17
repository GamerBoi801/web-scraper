import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.nike.com/w/mens-shoes-nik1zy7ok'  

#sending a GET request to the website
response = requests.get(url)

#checking if the request was successful
if response.status_code == 200:
    #HTML parser
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # every product have a div with class product-card
    products = soup.find_all('div', class_='product-card')  
    
    #extracting product names and prices
    data = []
    for product in products:
        name = product.find('div', class_='product-card__title').text.strip() if product.find('div', class_='product-card__title') else 'No Name'
        price = product.find('div', class_='product-price').text.strip() if product.find('div', class_='product-price') else '0'
        
        data.append({'Name': name, 'Price': price})

    #creating a DataFrame
    df = pd.DataFrame(data)

    # prints the  data frame
    print(df)
else:
    print('Failed to retrieve data.')
