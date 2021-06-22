import requests
import pprint
from bs4 import BeautifulSoup

wholefoods_addresses = ['1765 California St, San Francisco, CA 94109', '450 Rhode Island St, San Francisco, CA 94107', 
                        '690 Stanyan St, San Francisco, CA 94117', '2001 Market St, San Francisco, CA 94114', 
                        '399 4th St, San Francisco, CA 94107', '3950 24th St, San Francisco, CA 94114', 
                        '1150 Ocean Ave, San Francisco, CA 94112']

# ************  WHOLEFOODS RED WINES  ****************
URL = 'https://www.wholefoodsmarket.com/products/wine-beer-spirits/wine/red-wine'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='main-content')
# print(results.prettify())

reds_wf_images = results.find_all('img')
red_wines_wholefoods = results.find_all('div', class_='w-pie--product-tile__content')

wholefoods_reds = []
wf_reds_images = []
for red_wine in red_wines_wholefoods:
    brand = red_wine.find('span', class_='w-cms--font-disclaimer')
    name = red_wine.find('h3', class_='w-cms--font-body__sans-bold')
    wholefoods_reds.append(f"{brand.text} {name.text}")
print(wholefoods_reds)

for image in reds_wf_images:
    wf_reds_images.append(image['data-src'])


# *******  WHOLEFOODS WHITE WINES  ****************
URL = 'https://www.wholefoodsmarket.com/products/wine-beer-spirits/wine/white-wine'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='main-content')
# print(results.prettify())

whites_wf_images = results.find_all('img')
white_wines_wholefoods = results.find_all('div', class_='w-pie--product-tile__content')

wholefoods_whites = []
wf_whites_images = []
for white_wine in white_wines_wholefoods:
    brand = white_wine.find('span', class_='w-cms--font-disclaimer')
    name = white_wine.find('h3', class_='w-cms--font-body__sans-bold')
    wholefoods_whites.append(f"{brand.text} {name.text}")
print(wholefoods_whites)

for image in whites_wf_images:
    wf_whites_images.append(image['data-src'])

# *******  WHOLEFOODS PINK WINES  ****************
URL = 'https://www.wholefoodsmarket.com/products/wine-beer-spirits/wine/rose'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='main-content')
# print(results.prettify())

pinks_wf_images = results.find_all('img')
pink_wines_wholefoods = results.find_all('div', class_='w-pie--product-tile__content')

wholefoods_pinks = []
wf_pinks_images = []
for pink_wine in pink_wines_wholefoods:
    brand = pink_wine.find('span', class_='w-cms--font-disclaimer')
    name = pink_wine.find('h3', class_='w-cms--font-body__sans-bold')
    wholefoods_pinks.append(f"{brand.text} {name.text}")
print(wholefoods_pinks)

for image in pinks_wf_images:
    wf_pinks_images.append(image['data-src'])

# *******  WHOLEFOODS SPARKLING WINES  ****************
URL = 'https://www.wholefoodsmarket.com/products/wine-beer-spirits/wine/sparkling-wine'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='main-content')
# print(results.prettify())

sparkling_wf_images = results.find_all('img')
sparkling_wines_wholefoods = results.find_all('div', class_='w-pie--product-tile__content')

wholefoods_bubbles = []
wf_bubbles_images = []
for sparkling_wine in sparkling_wines_wholefoods:
    brand = sparkling_wine.find('span', class_='w-cms--font-disclaimer')
    name = sparkling_wine.find('h3', class_='w-cms--font-body__sans-bold')
    wholefoods_bubbles.append(f"{brand.text} {name.text}")
print(wholefoods_bubbles)

for image in sparkling_wf_images:
    wf_bubbles_images.append(image['data-src'])


# print('*************')
# print(wholefoods_reds)


# URL = 'https://www.safeway.com/shop/aisles/wine-beer-spirits/wine/wine-blends-other.1507.html?sort=&page=1'
# page = requests.get(URL)

# soup = BeautifulSoup(page.content, 'html.parser')
# results = soup.find(id='dynamic-product-grid-section')
# # print(results.prettify())

# #start fixing here
# red_wines_safeway = results.find_all('div', class_='dynamic-product-grid-section')

# for red_wine in red_wines_safeway:
#     title = red_wine.find('a', class_='title ftc')
#     # print(title.get('href'))
#     print(title.text)