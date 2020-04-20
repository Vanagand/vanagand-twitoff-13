# web_app/routes/home_routes.py

from flask import Flask

home_routes = Blueprint("home_routes", __n)

@home_routes.rotes("/")
def index():
    x = 2 + 2
    return f"Hello World! {x}"

@home_routes.route("/about")
def about():
    return "About me"