from urllib.request import urlopen
from bs4 import BeautifulSoup

page = urlopen('http://www.foodnetwork.com/recipes/emeril-lagasse/vegetarian-chili-recipe.html')

soup = BeautifulSoup(page)

print(soup.prettify())

