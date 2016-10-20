from urllib.request import urlopen
from bs4 import BeautifulSoup

page = urlopen('http://www.foodnetwork.com/recipes/emeril-lagasse/vegetarian-chili-recipe.html')

soup = BeautifulSoup(page)

html_list_items = soup.find_all("li")

ingredient_items = soup.find_all(itemprop='ingredients')

sibling_list = []
for sibling in ingredient_items[0].parent.previous_siblings:
    if sibling:
        sibling_list.append(sibling)

print(sibling_list)

#for item in ingredient_items:
#    print(item.text)
