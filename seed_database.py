"""Script to seed database."""

import os
import json

import crud
import model
import server

from random import choice

os.system('dropdb wines')
os.system('createdb wines')

model.connect_to_db(server.app)
model.db.create_all()

"""Generate 20 random wines."""
wine_list = []
for i in range(20):
    name = f'wine{i}'
    varietal = f'wine{i}'
    color = f'wine{i}'
    region = f'wine{i}'
    country = f'wine{i}'
    year_made = '2019'

    wine_list.append(crud.create_wine(name, varietal, color, region, country, year_made))    

"""Generate random users."""
for n in range(10):
    first_name = f'user{n}'
    last_name = f'user{n}'
    email = f'user{n}@test.com'
    password = 'test'

    user = crud.create_user(first_name, last_name, email, password)

    for _ in range(2):
        random_wine = choice(wine_list)
        print(user.wines)
        user.wines.append(random_wine)

"""Generate 5 random stores."""
for x in range(5):
    name = f'store{x}'
    location = f'location{x}'

    store = crud.create_store(name, location)

    # for _ in range(4):
    #     rand_wine = choice(wine_list)
    #     store.wines.append(rand_wine)
