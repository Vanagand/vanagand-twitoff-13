# web_app/__init__.py
# $env:FLASK_APP = "web_app"
# flask run

from flask import Flask

# app = Flask(__name__)

# @app.route("/") # handle requests to the home page
# def hello_world():
#     return "Hello, World!"

# @app.route("/about") # localhost:5000/about
# def about():
#     x = 2 + 2
#     return f"About me: {x}"

# # set FLASK_APP=app.py
# # flask run

from web_app.routes.home_routes import home_routes
from web_app.routes.book_routes import book_routes

# application factory pattern
def create_app():
    app = Flask(__name__)
    app.register_blueprint(home_routes)
    app.register_blueprint(book_routes)
    return app

if __name__ == "__main__":
    web_app = create_app()
    web_app.run(debug=True)
    