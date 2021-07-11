"""Script to seed database."""

import os
import json
import crud
import model
# from model import User, ...
import server
import store_data 
import requests
import sqlalchemy
from random import choice


# os.system('dropdb wines')
# os.system('createdb wines')

model.connect_to_db(server.app)
model.db.create_all()

GWS_API_KEY = os.environ.get('GWS_API_KEY')

# ********** CREATING STORES ************
try:
    for address in store_data.traderjoes_addresses:
        crud.create_store(name="Trader Joe's", location=address)
except sqlalchemy.exc.IntegrityError:
    model.db.session.rollback()


for address in store_data.safeway_addresses:
    try:
        crud.create_store(name="Safeway", location=address)
    except sqlalchemy.exc.IntegrityError:
        model.db.session.rollback()
        continue

for address in store_data.wholefoods_addresses:
    try:
        crud.create_store(name="Whole Foods Market", location=address)
    except sqlalchemy.exc.IntegrityError:
        model.db.session.rollback()
        continue
    

for address in store_data.costco_address:
    try:
        crud.create_store(name="Costco", location=address)
    except sqlalchemy.exc.IntegrityError:
        model.db.session.rollback()
        continue

for address in store_data.flatiron_address:
    try:
        crud.create_store(name="Flatiron Wines & Spirits", location=address)
    except sqlalchemy.exc.IntegrityError:
        model.db.session.rollback()
        continue

for address in store_data.sfwtc_address:
    try:
        crud.create_store(name="San Francisco Wine Trading Co.", location=address)
    except sqlalchemy.exc.IntegrityError:
        model.db.session.rollback()
        continue

for address in store_data.rainbow_address:
    try:
        crud.create_store(name="Rainbow Grocery", location=address)
    except sqlalchemy.exc.IntegrityError:
        model.db.session.rollback()
        continue

for address in store_data.birite_addresses:
    try:
        crud.create_store(name="Bi-Rite Market", location=address)
    except sqlalchemy.exc.IntegrityError:
        model.db.session.rollback()
        continue



# ******* CREATING WHOLE FOODS WINES *********
for index, wine in enumerate(store_data.wholefoods_reds):
    crud.create_wine(name=wine, url=store_data.wf_reds_images[index], color='red')
    
for index, wine in enumerate(store_data.wholefoods_whites):
    crud.create_wine(name=wine, url=store_data.wf_whites_images[index], color='white')

for index, wine in enumerate(store_data.wholefoods_pinks):
    crud.create_wine(name=wine, url=store_data.wf_pinks_images[index], color='pink')

for index, wine in enumerate(store_data.wholefoods_bubbles):
    crud.create_wine(name=wine, url=store_data.wf_bubbles_images[index], color='white')

# ************ CREATING RED WINES FROM API **************

url = 'https://api.globalwinescore.com/globalwinescores/latest/'

params = {
        # 'wine': name,
        'color': 'red',
        # 'vintage': vintage,
        'country': 'Usa',
        'appellation': 'Napa Valley',
        'limit': 150,
        # 'ordering': '-score'
        }
   
headers = {
        'Authorization': GWS_API_KEY
    }

response = requests.get(url, params=params, headers=headers)
red_results = response.json()
# print(red_results)
red_images = ['https://oakvillegrocery.com/media/catalog/product/cache/636ef36f03333a69b7b5461c2b2beca4/n/v/nv_1881_sparklingwine_700x700.png',
              'https://oakvillegrocery.com/media/catalog/product/cache/636ef36f03333a69b7b5461c2b2beca4/n/v/nv_amusebouche_napa_redwine_700x700_1.png',
              'https://oakvillegrocery.com/media/catalog/product/cache/636ef36f03333a69b7b5461c2b2beca4/n/v/nv_surrealist_700x700.png',
              'https://oakvillegrocery.com/media/catalog/product/cache/636ef36f03333a69b7b5461c2b2beca4/n/v/nv_continuum_sagemountain_propred_napa_700x700_1.png',
              'https://oakvillegrocery.com/media/catalog/product/cache/636ef36f03333a69b7b5461c2b2beca4/n/v/nv_stsupery_rutherford_cab_700x700.png',
              'https://oakvillegrocery.com/media/catalog/product/cache/636ef36f03333a69b7b5461c2b2beca4/n/v/nv_1881_calistoga_cab_700x700.png',
              'https://oakvillegrocery.com/media/catalog/product/cache/636ef36f03333a69b7b5461c2b2beca4/2/0/2015_portfolio_napavalley_700x700.png',
              'https://oakvillegrocery.com/media/catalog/product/cache/636ef36f03333a69b7b5461c2b2beca4/n/v/nv_melka_mekerra_napavalley_red_700x700.png',
              'https://oakvillegrocery.com/media/catalog/product/cache/636ef36f03333a69b7b5461c2b2beca4/n/v/nv_dunn_howellmtn_cab_700x700.png',
              'https://oakvillegrocery.com/media/catalog/product/cache/636ef36f03333a69b7b5461c2b2beca4/n/v/nv_macauley_reservecab_700x700.png',
              'https://oakvillegrocery.com/media/catalog/product/cache/636ef36f03333a69b7b5461c2b2beca4/2/0/2017_rudd_crossroads_cab_700x700.png',
              'https://oakvillegrocery.com/media/catalog/product/cache/636ef36f03333a69b7b5461c2b2beca4/n/v/nv_lail_blueprint_cab_700x700_1.png',
              'https://oakvillegrocery.com/media/catalog/product/cache/636ef36f03333a69b7b5461c2b2beca4/o/r/orin.png',
              'https://oakvillegrocery.com/media/catalog/product/cache/636ef36f03333a69b7b5461c2b2beca4/n/v/nv_mascot_oakville_cab_700x700.png',
              'https://oakvillegrocery.com/media/catalog/product/cache/636ef36f03333a69b7b5461c2b2beca4/2/0/2017_harlan_estate_cab..png']

for result in red_results['results']:
    name = result['wine']
    url = choice(red_images)
    color = result['color']
    vintage = result['vintage']
    country = result['country']
    region = result['appellation']
    crud.create_wine(name=name, url=url, color=color, vintage=vintage, country=country, region=region)

# *************** CREATING WHITE WINES FROM API **************

url = 'https://api.globalwinescore.com/globalwinescores/latest/'

params = {
        # 'wine': name,
        'color': 'white',
        # 'vintage': vintage,
        'country': 'France',
        # 'appellation': 'Napa Valley',
        'limit': 100,
        # 'ordering': '-score'
        }
   
headers = {
        'Authorization': GWS_API_KEY
    }

response = requests.get(url, params=params, headers=headers)
white_results = response.json()

white_images = ['https://products0.imgix.drizly.com/ci-patient-cottat-anc-vig-sancere-20a4a26955cf38b9.jpeg?auto=format%2Ccompress&ch=Width%2CDPR&dpr=2&fm=jpg&h=240&q=20',
                'https://products1.imgix.drizly.com/ci-dom-paul-buisse-touraine-sauvignon-dd7c492dcbe76f82.jpeg?auto=format%2Ccompress&ch=Width%2CDPR&dpr=2&fm=jpg&h=240&q=20',
                'https://products3.imgix.drizly.com/ci-la-forcine-sancerre-c41f4dd28498153d.jpeg?auto=format%2Ccompress&ch=Width%2CDPR&dpr=2&fm=jpg&h=240&q=20',
                'https://products1.imgix.drizly.com/ci-domaine-de-la-pepiere-muscadet-sevre-et-maine-sur-lie-ab9565c2aa84542e.jpeg?auto=format%2Ccompress&ch=Width%2CDPR&dpr=2&fm=jpg&h=240&q=20',
                'https://products2.imgix.drizly.com/ci-xavier-flouret-french-blonde-sancerre-686ecdc8cc3d1d0f.jpeg?auto=format%2Ccompress&ch=Width%2CDPR&dpr=2&fm=jpg&h=240&q=20',
                'https://products1.imgix.drizly.com/ci-mary-taylor-anjou-blanc-6fb8df8c0a3c86cf.png?auto=format%2Ccompress&ch=Width%2CDPR&dpr=2&fm=jpg&h=240&q=20',
                'https://products2.imgix.drizly.com/ci-claude-riffault-sancerre-les-boucauds-2015-baddfd47fe4b6dc2.jpeg?auto=format%2Ccompress&ch=Width%2CDPR&dpr=2&fm=jpg&h=240&q=20',
                'https://products0.imgix.drizly.com/ci-les-deux-moulins-sauvignon-blanc-0d62290bff0b12e0.jpeg?auto=format%2Ccompress&ch=Width%2CDPR&dpr=2&fm=jpg&h=240&q=20',
                'https://products2.imgix.drizly.com/ci-latour-corton-charlemagne-1a83195fe4c951c4.jpeg?auto=format%2Ccompress&ch=Width%2CDPR&dpr=2&fm=jpg&h=240&q=20',
                'https://products0.imgix.drizly.com/ci-varnier-fanniere-cuvee-saint-denis-grand-cru-brut-5feacdf62d057f42.jpeg?auto=format%2Ccompress&ch=Width%2CDPR&dpr=2&fm=jpg&h=240&q=20']

for result in white_results['results']:
    name = result['wine']
    url = choice(white_images)
    color = result['color']
    vintage = result['vintage']
    country = result['country']
    region = result['appellation']
    crud.create_wine(name=name, url=url, color=color, vintage=vintage, country=country, region=region)


# ***************** CREATING PINK WINES FROM API ***************

url = 'https://api.globalwinescore.com/globalwinescores/latest/'

params = {
        # 'wine': name,
        'color': 'pink',
        # 'vintage': vintage,
        'country': 'France',
        # 'appellation': 'Napa Valley',
        'limit': 50,
        # 'ordering': '-score'
        }
   
headers = {
        'Authorization': GWS_API_KEY
    }

response = requests.get(url, params=params, headers=headers)
pink_results = response.json()

pink_images = ['https://products0.imgix.drizly.com/ci-fleurs-de-prairie-rose-f120461895576ade.png?auto=format%2Ccompress&ch=Width%2CDPR&dpr=2&fm=jpg&h=240&q=20',
               'https://products3.imgix.drizly.com/ci-francis-coppola-sofia-rose-53e10031e1f56bf2.jpeg?auto=format%2Ccompress&ch=Width%2CDPR&dpr=2&fm=jpg&h=240&q=20',
               'https://products1.imgix.drizly.com/ci-villa-wolf-rose-pinot-noir-2014-e5252910685a82f7.png?auto=format%2Ccompress&ch=Width%2CDPR&dpr=2&fm=jpg&h=240&q=20',
               'https://products1.imgix.drizly.com/ci-the-little-sheep-rose-6d1913cc45f164c0.jpeg?auto=format%2Ccompress&ch=Width%2CDPR&dpr=2&fm=jpg&h=240&q=20',
               'https://products0.imgix.drizly.com/ci-chateau-castel-des-maures-rose-64e1a0df1902fc33.jpeg?auto=format%2Ccompress&ch=Width%2CDPR&dpr=2&fm=jpg&h=240&q=20']

for result in pink_results['results']:
    name = result['wine']
    url = choice(pink_images)
    color = result['color']
    vintage = result['vintage']
    country = result['country']
    region = result['appellation']
    crud.create_wine(name=name, url=url, color=color, vintage=vintage, country=country, region=region)

all_wines = crud.get_all_wines()

whole_foods = crud.get_stores_by_name('Whole Foods Market')
safeway = crud.get_stores_by_name('Safeway')
costco = crud.get_stores_by_name('Costco')
flatiron = crud.get_stores_by_name('Flatiron Wines & Spirits')
sfwtc = crud.get_stores_by_name('San Francisco Wine Trading Co.')
rainbow = crud.get_stores_by_name('Rainbow Grocery')
birite = crud.get_stores_by_name('Bi-Rite Market')
tjs = crud.get_stores_by_name("Trader Joe's")

for store in whole_foods:
    for wine in all_wines:
        if (wine.wine_id <= 190):
            crud.seed_stores_and_wines(wine, store)

for store in safeway:
    for wine in all_wines:
        if (wine.wine_id <= 350):
            crud.seed_stores_and_wines(wine, store)

for store in costco:
    for wine in all_wines:
        if (wine.wine_id > 100) and (wine.wine_id < 350):
            crud.seed_stores_and_wines(wine, store)

for store in flatiron:
    for wine in all_wines:
        crud.seed_stores_and_wines(wine, store)

for store in sfwtc:
    for wine in all_wines:
        crud.seed_stores_and_wines(wine, store)

for store in rainbow:
    for wine in all_wines:
        if (wine.wine_id > 410):
            crud.seed_stores_and_wines(wine, store)

for store in birite:
    for wine in all_wines:
        if (wine.wine_id > 120) and (wine.wine_id < 220):
            crud.seed_stores_and_wines(wine, store)

for store in tjs:
    for wine in all_wines:
        if (wine.wine_id > 170) and (wine.wine_id < 370):
            crud.seed_stores_and_wines(wine, store)



# for store in stores:
#     for wine in wines:
#         crud.seed_stores_and_wines(wine, store)

# if store.name == 'Whole Foods Market':
#     for wine in wines:
#         crud.seed_stores_and_wines(wine, store)


