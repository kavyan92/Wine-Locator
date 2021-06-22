"""Script to seed database."""

import os
import json

import crud
import model
# from model import User, ...
import server
import store_data 

from random import choice

os.system('dropdb wines')
os.system('createdb wines')

model.connect_to_db(server.app)
model.db.create_all()

# """Generate 20 random wines."""
# wine_list = []
# for i in range(20):
#     name = f'wine{i}'
#     # varietal = f'wine{i}'
#     color = f'wine{i}'
#     region = f'wine{i}'
#     country = f'wine{i}'
#     vintage = '2019'

#     wine_list.append(crud.create_wine(name, url, color, region, country, vintage))    

# """Generate random users."""
# for n in range(10):
#     first_name = f'user{n}'
#     last_name = f'user{n}'
#     email = f'user{n}@test.com'
#     password = 'test'

#     user = crud.create_user(first_name, last_name, email, password)

#     for _ in range(2):
#         random_wine = choice(wine_list)
#         user.wines.append(random_wine)

# """Generate 5 random stores."""
# for x in range(5):
#     name = f'store{x}'
#     location = f'location{x}'

#     store = crud.create_store(name, location)

#     for _ in range(4):
#         rand_wine = choice(wine_list)
#         store.wines.append(rand_wine)

# print('*'*20)
# print(store_data.wholefoods_reds)
# print('*'*20)

for index, wine in enumerate(store_data.wholefoods_reds):
    crud.create_wine(name=wine, url=store_data.wf_reds_images[index], color='red')
    
for index, wine in enumerate(store_data.wholefoods_whites):
    crud.create_wine(name=wine, url=store_data.wf_whites_images[index], color='white')

for index, wine in enumerate(store_data.wholefoods_pinks):
    crud.create_wine(name=wine, url=store_data.wf_pinks_images[index], color='pink')

for index, wine in enumerate(store_data.wholefoods_bubbles):
    crud.create_wine(name=wine, url=store_data.wf_bubbles_images[index], color='white')

for address in store_data.wholefoods_addresses:
    crud.create_store(name='Whole Foods Market', location=address)

stores = crud.get_stores_by_name('Whole Foods Market')
wines = crud.get_all_wines()

for store in stores:
    for wine in wines:
        crud.seed_stores_and_wines(wine, store)

# if store.name == 'Whole Foods Market':
#     for wine in wines:
#         seed_stores_and_wines(wine, store)


