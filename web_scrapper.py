from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import re

page = urlopen(Request( 'http://www.epicurious.com/recipes/food/views/guacamole-13592',
		headers={'User-Agent': 'Magic Browser'}))

url3 = 'http://allrecipes.com/recipe/95753/funky-enchilada-casserole/?internalSource=rotd&referringId=1218&referringContentType=recipe%20hub&clickId=cardslot%201'
url2 = 'http://www.simplyrecipes.com/recipes/enchiladas/'
other_url = 'http://www.foodnetwork.com/recipes/emeril-lagasse/vegetarian-chili-recipe.html'

soup = BeautifulSoup(page)

html_list_items = soup.find_all("li")

ingredients_re = re.compile('ingredients', re.I)
ingredient_re = re.compile('ingredient', re.I)
ingredient_items = soup.find_all(itemprop=ingredient_re) + soup.find_all(class_=ingredient_re) + soup.find_all(id=ingredient_re)

ingredient_header = soup.find_all(re.compile('h\d'), string=ingredients_re)

header_siblings = ingredient_header[0].find_next_siblings()

ingredients = []
for item in header_siblings:
    ingredients.extend(item.find_all("li"))


#for item in ingredient_items:
#    if item.name == 'li':
#        ingredients.append(item.text)

sibling_list = []
for sibling in ingredient_items[0].parent.previous_siblings:
    if sibling:
        sibling_list.append(sibling)

print(ingredients)

#for item in ingredient_items:
#    print(item.text)

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
