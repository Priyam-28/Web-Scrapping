import requests
from bs4 import BeautifulSoup as bs

search_url = f"https://www.flipkart.com/search?q="+"iphone12pro"
response = requests.get(search_url)

print(response.text)