import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL for the target Nike products page (replace with an actual URL)
url = 'https://www.nike.com/in/w/mens-shoes-nik1zy7ok'  # Example URL; make sure this path is allowed in robots.txt

# GET request to the website
response = requests.get(url)

# Check to see if the request was successful
if response.status_code == 200:
    
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all product containers (adjust class name based on actual HTML structure)
    products = soup.find_all('a', class_="product-card product-grid__card  css-1tmiin5")  # Ensure this class matches Nike's HTML structure

    # Extracting product names and prices
    data = []
    for product in products:
        name = product.find('div', class_='product-card__title').text.strip() if product.find('h2', class_='product-card__title') else 'No Name'
        price = product.find('div', class_='product-price in__styling is--current-price css-11s12ax').text.strip() if product.find('div', class_='product-price in__styling is--current-price css-11s12ax') else '0'
        
        # Debug print to check what is being extracted
        print(f"Extracted - Name: {name}, Price: {price}")
        
        data.append({'Name': name, 'Price': price})

    # Creating a DataFrame
    df = pd.DataFrame(data)

    # Print the DataFrame to check its contents
    print(df)

    # Check for Price column existence and process it if it exists
    if 'Price' in df.columns:
        # Remove currency symbols and convert prices to float
        df['Price'] = df['Price'].replace({'\$': '', ',': ''}, regex=True)
        df['Price'] = df['Price'].apply(float)

        # Check for missing values and drop if there are any
        df.dropna(inplace=True)

        # Print basic statistics about the data
        print(df.describe())
    else:
        print("Price column does not exist. Please check data extraction.")
else:
    print('Failed to retrieve data.')
