import csv
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

urlToScrap = "https://www.flipkart.com/search?q=laptop&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&as-pos=1&as-type=RECENT&suggestionId=laptop%7CLaptops&requestId=7ec220e8-4f02-4150-9e0b-9e90cf692f4b&as-searchtext=laptop"

response = requests.get(urlToScrap)
pageContent = response.content  # the page html content
document = bs(pageContent, "html.parser")
# print(document.prettify())


products = []  # holding the products titles
prices = []  # holding the products prices
ratings = []  # hodling the prodocuts ratings

for iterator in document.findAll('a', href=True, attrs={'class': "_1fQZEK"}):
    name = iterator.find('div', attrs={'class': '_4rR01T'})
    price = iterator.find('div', attrs={'class': '_30jeq3 _1_WHN1'})
    rating = iterator.find('div', attrs={'class': '_3LWZlK'})
    products.append(name.text)
    prices.append(price.text)
    ratings.append(rating.text)


outputDocument = pd.DataFrame(
    {'Product Name': products, 'Product Price': prices, 'Product Rating': ratings})
outputDocument.head()
outputDocument.to_csv('products.csv')  # generating csv file

# product=document.find('div',attrs={'class':'_4rR01T'})  # extract product title
# print(product.text)
