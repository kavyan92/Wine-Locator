"""CRUD operations."""

from model import db, connect_to_db, User, Wine, Store

def create_user(first_name, last_name, email, password):
    """Create and return a new user."""

    user = User(first_name=first_name, last_name=last_name, email=email, password=password)
    
    db.session.add(user)
    db.session.commit()

    return user

def get_users():
    """Return all users."""

    return User.query.all()

def get_user_by_id(user_id):
    """Return a user by primary key."""

    return User.query.get(user_id)

def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter_by(email = email).first()

def create_wine(name, url, color, region=None, country=None, vintage=None):
    """Create and return a new wine."""

    wine = Wine(name=name, url=url, color=color, region=region,
                country=country, vintage=vintage)

    db.session.add(wine)
    db.session.commit()

    return wine

def get_all_wines():
    """Return all wines."""

    return Wine.query.all()

def get_wine_by_id(wine_id):
    """Return wine by primary key."""

    return Wine.query.get(wine_id)

def get_wines_by_region(region):
    """Return wines by region."""

    return Wine.query.filter(Wine.region == region).all()

def get_wines_by_country(country):
    """Return all wines from a country."""

    return Wine.query.filter(Wine.country == country).all()

def get_wines_by_color(color):
    """Return all wines by color."""

    return Wine.query.filter(Wine.color == color).all()

def get_wines_by_user(user_id):
    """Return all wines liked by a user."""

    user = User.query.get(user_id)

    return user.wines

def create_store(name, location):
    """Create and return a new store."""

    store = Store(name=name, location=location)

    db.session.add(store)
    db.session.commit()

    return store

def get_all_stores():
    """Return all stores in database."""

    return Store.query.all()

def get_stores_by_name(name):
    """Return all stores by name."""

    return Store.query.filter(Store.name == name).all()

def get_wines_by_store(store_id):
    """Get all wines available at a certain store."""

    store = Store.query.get(store_id)

    return store.wines

def get_stores_by_wine(wine_id):
    """Get all stores that sell a certain wine."""
    
    wine = Wine.query.get(wine_id)

    return wine.stores

def get_store_by_id(store_id):
    """Get store by store id."""

    store = Store.query.get(store_id)

    return store

def seed_users_and_wines(wine, user):
    """Save wines a user likes to that user."""
    
    user.wines.append(wine)
    db.session.add(user)
    db.session.commit()
    return user.wines

def seed_stores_and_wines(wine, store):
    """Save wines a store sells to that store."""

    store.wines.append(wine)
    db.session.add(store)
    db.session.commit()
    return store.wines

# if __name__ == '__main__':
#     from server import app
#     connect_to_db(app) # we should get rid of