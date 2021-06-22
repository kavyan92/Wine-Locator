"""Server for wine locator app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect, jsonify)
from model import db, connect_to_db, User
import crud
import os
from random import choice

from jinja2 import StrictUndefined
import requests
app = Flask(__name__)   
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

GWS_API_KEY = os.environ.get('GWS_API_KEY')
@app.route("/")
def homepage():
    """Display homepage."""

    all_wines = crud.get_all_wines()
    wines = []
    for _ in range(20):
        wines.append(choice(all_wines))
   
    return render_template('homepage.html', wines=wines)

@app.route("/results", methods=["GET"])
def search():
    """Display search results based on user input properties."""

    url = 'https://api.globalwinescore.com/globalwinescores/latest/'
    # params = {
    #     'wine_id': wine_id, # allows for multiple wine_ids to be queried
    #     'color': color,
    #     'vintage': vintage,
    #     'country': country,
    #     'appellation': appellation,
    #     'limit': # explicitly set to 10 or ask user w/ request.form.get('result_limit'),
    #     'ordering': '-score' or '-date'
    # }

    name = request.args.get("wine_name")
    color = request.args.get("color")
    vintage = request.args.get("vintage")  
    country = request.args.get("country")
    region = request.args.get("region")
    
    print(name, '&&&&&&&&&&& NAME')

    params = {
        # 'wine': name,
        'color': color,
        'vintage': vintage,
        'country': country,
        'appellation': region,
        'limit': 1000,
        # 'ordering': '-score'
        }
   
    headers = {
        'Authorization': GWS_API_KEY
    }

    response = requests.get(url, params=params, headers=headers)
    results = response.json()

    search_results = [] 
    if name:
        for result in results['results']:
            print(result)
            if name.lower() in result['wine'].lower():
                search_results.append(result)
                
    else:
        search_results = results

    print(search_results)
    return render_template('results.html', results=results, search_results=search_results, name=name)
    
@app.route("/wines")
def all_wines():
    """View all wines."""

    wines = crud.get_all_wines()

    return render_template("all_wines.html", wines=wines)

@app.route("/wines/<wine_id>")
def show_wine(wine_id):
    """Show details on a particular wine."""

    wine = crud.get_wine_by_id(wine_id)
    
    return render_template("wine_details.html", wine=wine)

@app.route("/wines/<wine_id>", methods=["POST"])
def save_wine_to_user(wine_id):
    """Save wine a user likes to their profile."""
    
    wine_id = request.form.get('wine-id')
    wine = crud.get_wine_by_id(wine_id)
    user = crud.get_user_by_id(session["user"])
  
    if user:
        # print(user.wines)
        if wine in user.wines:
            flash("You have already liked this wine!")
            print("You have already liked this wine!")
        else: 
            user_wines = crud.seed_users_and_wines(wine, user)
            # print(user_wines)
            flash("Wine saved!")
    else:
        flash("You must be logged in to save wines!")
        return redirect("/login")

    # # anticipating duplicates, fix!
    return redirect("/my_wines")

@app.route("/my_wines")
def show_user_profile():
    """Display logged in user's saved wines."""
    if 'user' in session:
        user_id = session['user']
        user = crud.get_user_by_id(user_id)
        wines = user.wines
    else: 
        return redirect("/login")

    return render_template("my_wines.html", user=user, wines=wines)

@app.route("/my_wines", methods=["POST"])
def remove_saved_wine():
    """Remove a wine from logged in user's saved wines."""
    
    wine_id = request.form.get("wine-id")
    wine = crud.get_wine_by_id(wine_id)
    user_id = session['user']
    user = crud.get_user_by_id(user_id)
    user.wines.remove(wine)
    db.session.commit()
    
    return redirect("/my_wines")

@app.route("/signup")
def sign_up():
    """Display sign up form."""
 
    return render_template("signup.html")

@app.route("/signup", methods=["POST"])
def create_account():
    """Create a new user."""

    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")
    password = request.form.get("password")
    
    user = crud.get_user_by_email(email) # user doesn't exist yet

    if user:
        print("An account with that email already exists. Please use another email.")
        flash("An account with that email already exists. Please use another email.")

        return render_template("/signup.html")
    else:
        crud.create_user(first_name, last_name, email, password)
        print("Account created.")
        flash("Account successfully created! Please log in.")

        return redirect("/login")


@app.route("/login")
def login():
    """Display login page."""

    return render_template("login.html")

@app.route("/login", methods=["POST"])
def process_login():
    """Process user login."""

    email = request.form.get("email")
    password = request.form.get("password")
  
    user = crud.get_user_by_email(email)

    if not user or user.password != password:
        flash("The email or password entered was incorrect. Please try again.")

        return render_template("/login.html")
    else:
        # Log in user by storing the user's email in session
        session["user"] = user.user_id
        print(f"Welcome back, {user.first_name} {user.last_name}!")
        flash(f"Welcome back, {user.first_name} {user.last_name}!")

        return redirect("/")

@app.route("/logout")

def process_logout():
    """Log the current user out."""

    if session.get("user"):
        del session["user"]
    flash("You are logged out.")

    return redirect("/")

@app.route("/stores/<store_id>")
def show_store(store_id):
    """Show details about a particular store."""

    store = crud.get_store_by_id(store_id)

    return render_template("store_details.html", store=store)


if __name__ == '__main__':
    connect_to_db(app)
    app.run(use_reloader=True, use_debugger=True)

# if __name__ == '__main__':
#     connect_to_db(app)
#     app.run(host='127.0.0.1', debug=True)