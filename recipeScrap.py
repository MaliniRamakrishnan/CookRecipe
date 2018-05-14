import pandas as pd
import requests
import array
from bs4 import BeautifulSoup
cook_response = requests.get("https://www.101cookbooks.com/archives.html")
soup = BeautifulSoup(cook_response.content, 'html.parser')
#print(soup.prettify()) #prints the whole page
main_recipe_list = soup.find(id="archives")
title_items = main_recipe_list.find_all('div',class_="archiverecipe")
cook_items_url = [item.find("a")['href'] for item in title_items] #prints URLs in an array format
#print(len(cook_items_url))
recipe_ingredients = []
count = 0
for item_url in cook_items_url:
    item_response = requests.get(item_url)
    #item_response = requests.get(cook_items_url[0])
    item_soup = BeautifulSoup(item_response.content, 'html.parser')
    recipe_data = item_soup.find('div',id="recipe")
    recipe_name = recipe_data.find("h1").get_text()
    print(recipe_name)
    recipe_ingredients.append(recipe_name + "::" + recipe_data.find("p").get_text())
    count = count + 1
    if count > 10 :
        break;
print(recipe_ingredients)
