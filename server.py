"""Server for wine locator app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db
import crud

from jinja2 import StrictUndefined
# import requests

# wine_db = requests.get('https://api.globalwinescore.com/globalwinescores/latest/')
# wine_db.json()
# payload = {"key": "Token 58dff4aa485c672bfc7b552cd2694124d9484fbe", 

app = Flask(__name__)   
# app.secret_key = "dev"
# app.jinja_env.undefined = StrictUndefined

@app.route("/")
def homepage():
    """Display homepage."""

    return render_template('homepage.html')

# @app.route("/search")
# def search():
#     """View search results based on user input properties."""

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

# @app.route("/users")
# def all_users():
#     """View all users."""

#     users = crud.get_users()

#     return render_template("all_users.html", users=users)

@app.route("/signup")
def sign_up():
    """Display Sign Up form."""

    return render_template("signup.html")

@app.route("/signup", methods=["POST"])
def create_account():
    """Create a new user."""

    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")
    password = request.form.get("password")
    print(email)
    user = crud.get_user_by_email(email)
   
    print(user)
    if user:
        flash("An account with that email already exists. Please use another email.")
    else:
        crud.create_user(first_name, last_name, email, password)
        flash("Account successfully created! Please log in.")

    return redirect("/login")

@app.route("/users/<user_id>")
def show_user(user_id):
    """Show details about a particular user."""

    user = crud.get_user_by_id(user_id)

    return render_template("user_details.html", user=user)

# is this correct??
# @app.route("/users/<user_id>/mywines") 
# def my_wines()
#     """Display logged in user's saved wines."""

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
    else:
        # Log in user by storing the user's email in session
        session["user"] = user.user_id
        flash(f"Welcome back, {user.first_name} {user.last_name}!")

    return redirect("/")




if __name__ == '__main__':
    connect_to_db(app)
    app.run(use_reloader=True, use_debugger=True)

# if __name__ == '__main__':
#     connect_to_db(app)
#     app.run(host='0.0.0.0', debug=True)