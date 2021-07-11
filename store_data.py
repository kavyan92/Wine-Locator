import requests
import crud
import pprint
from bs4 import BeautifulSoup

traderjoes_addresses = ['265 Winston Dr, San Francisco, CA 94132', '3 Masonic Ave, San Francisco, CA 94118',
                        '555 9th St, San Francisco, CA 94103', '10 4th St, San Francisco, CA 94103', 
                        '1095 Hyde St, San Francisco, CA 94109', '401 Bay St, San Francisco, CA 94133']

safeway_addresses = ['4950 Mission St, San Francisco, CA 94112', '625 Monterey Blvd, San Francisco, CA 94127', 
                     '3350 Mission St, San Francisco, CA 94110', '5290 Diamond Heights Blvd, San Francisco, CA 94131', 
                     '730 Taraval St, San Francisco, CA 94116', '2350 Noriega St, San Francisco, CA 94122', 
                     '850 La Playa St, San Francisco, CA 94121', '735 7th Ave, San Francisco, CA 94118', 
                     '2020 Market St, San Francisco, CA 94114', '1335 Webster St, San Francisco, CA 94115', 
                     '2300 16th St Unit 203, San Francisco, CA 94103', '298 King St, San Francisco, CA 94107', 
                     '145 Jackson St, San Francisco, CA 94111', '15 Marina Blvd, San Francisco, CA 94123']

wholefoods_addresses = ['1765 California St, San Francisco, CA 94109', '450 Rhode Island St, San Francisco, CA 94107', 
                        '690 Stanyan St, San Francisco, CA 94117', '2001 Market St, San Francisco, CA 94114', 
                        '399 4th St, San Francisco, CA 94107', '3950 24th St, San Francisco, CA 94114', 
                        '1150 Ocean Ave, San Francisco, CA 94112']

costco_address = ['450 10th St, San Francisco, CA 94103']

flatiron_address = ['2 New Montgomery St, San Francisco, CA 94105']

sfwtc_address = ['250 Taraval St, San Francisco, CA 94116']

rainbow_address = ['1745 Folsom St, San Francisco, CA 94103']

birite_addresses = ['3639 18th St, San Francisco, CA 94110', '550 Divisadero St, San Francisco, CA 94117']

# ************  WHOLEFOODS RED WINES  ****************
URL = 'https://www.wholefoodsmarket.com/products/wine-beer-spirits/wine/red-wine'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='main-content')
# print(results.prettify())

reds_wf_images = results.find_all('img')
red_wines_wholefoods = results.find_all('div', class_='w-pie--product-tile__content')
red_prices = results.find_all('div', class_='w-pie--prices')
# print(red_prices)

wholefoods_reds = []
wf_reds_images = []
for red_wine in red_wines_wholefoods:
    brand = red_wine.find('span', class_='w-cms--font-disclaimer')
    name = red_wine.find('h3', class_='w-cms--font-body__sans-bold')
    wholefoods_reds.append(f"{brand.text} {name.text}") 
# print(wholefoods_reds)

# for el in red_prices:
#     cost = el.find_all('span', class_='regular_price')
#     reds_prices.append(f"{cost.text}")
# print(reds_prices)

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
# print(wholefoods_whites)

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

#### start  here
pinks_prices = []
wholefoods_pinks = []
wf_pinks_images = []
for pink_wine in pink_wines_wholefoods:
    brand = pink_wine.find('span', class_='w-cms--font-disclaimer')
    name = pink_wine.find('h3', class_='w-cms--font-body__sans-bold')
    wholefoods_pinks.append(f"{brand.text} {name.text}")
    wholefoods_pinks
# print(wholefoods_pinks)

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
# print(wholefoods_bubbles)

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