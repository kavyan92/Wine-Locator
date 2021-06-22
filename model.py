"""Models for wine locator app."""
# from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

user_wine_association_table = db.Table('users_wines',
    db.Column('user_id', db.Integer, db.ForeignKey('users.user_id')),
    db.Column('wine_id', db.Integer, db.ForeignKey('wines.wine_id'))
)

store_wine_association_table = db.Table('stores_wines',
    db.Column('store_id', db.Integer, db.ForeignKey('stores.store_id')),
    db.Column('wine_id', db.Integer, db.ForeignKey('wines.wine_id'))
)

class User(db.Model):
    """A user."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    first_name = db.Column(db.String(25))
    last_name = db.Column(db.String(25))
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    def __repr__(self):
        return f'<User user_id={self.user_id} first_name={self.first_name} last_name={self.last_name} email={self.email}>'


class Wine(db.Model):
    """A wine."""

    __tablename__ = 'wines'

    wine_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    name = db.Column(db.String)
    url = db.Column(db.String)
    color = db.Column(db.String(25))
    region = db.Column(db.String(25))
    country = db.Column(db.String(25))
    vintage = db.Column(db.Integer)

    # establish relationship with user and store table
    user = db.relationship('User', 
                            secondary=user_wine_association_table,
                            backref='wines')

    stores = db.relationship('Store',
                            secondary=store_wine_association_table,
                            backref='wines')

    def __repr__(self):
        return f'<Wine wine_id={self.wine_id} name={self.name} region={self.region}>'


class Store(db.Model):
    """A store."""

    __tablename__ = 'stores'

    store_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    name = db.Column(db.String)
    location = db.Column(db.String, unique=True)

    def __repr__(self):
        return f'<Store store_id={self.store_id} name={self.name} location={self.location}>'

    
# def connect_to_db(app, db_uri='postgresql:///wines', echo=True):
#     flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
#     flask_app.config['SQLALCHEMY_ECHO'] = False
#     flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#     db.app = flask_app
#     db.init_app(app)

#     print("Connected to the db!")

def connect_to_db(app):
    """Connect the database to our Flask app."""

    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///wines"
    app.config["SQLALCHEMY_ECHO"] = False
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)

if __name__ == '__main__':
    from server import app
    connect_to_db(app)