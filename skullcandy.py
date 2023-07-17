
# # Testing with Skull Candy site - Working!
import requests
from bs4 import BeautifulSoup

def replaceSpace(string):
    return string.replace(" ", "%20")

def scrape_site(search_query):
    
    newQuery = replaceSpace(search_query)
    # Set up the search URL with the provided query
    search_url = f'https://www.skullcandy.ca/search.php?search_query={newQuery}&section=product'

    # Send a GET request to the search URL
    response = requests.get(search_url)

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the search result items
    search_results = soup.find_all('article', class_='product-card card')

    # Initialize lists to store the product names and prices
    product_names = []
    prices = []

    # Extract the name and price for each search result item
    for result in search_results:
        # Extract the product name
        name_element = result.find('h4', {'class': 'card-title'})
        if name_element:
            product_names.append(name_element.text.strip())

        # Extract the product price
        price_category = result.find('div', {'class': 'card-text'})
        price_element = price_category.find('span')
        if price_element:
            prices.append(price_element.text.strip())

        # Break the loop after retrieving the top 3 results
        if len(product_names) >= 3:
            break

    # Print the product names and prices
    for name, price in zip(product_names, prices):
        print(f'Product: {name} | Price: {price}')


#Test
search_query = 'bluetooth headphones'
scrape_site(search_query)