# web_app/__init__.py
# $env:FLASK_APP = "web_app" > flask run

from flask import Flask

from web_app.models import db, migrate
from web_app.routes.home_routes import home_routes
from web_app.routes.book_routes import book_routes

DATABASE_URI = "sqlite:////Users/Michel/Desktop/lambda_ds13/vanagand-twitoff-13/web_app/twitoff_13.db"
SECRET_KEY = "Super secret" # (TODO: read from .env var)

# application factory pattern
def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = SECRET_KEY # required for flash messaging

    # In case of failure delete .db and run code
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False # suppress warning messages

    db.init_app(app)
    migrate.init_app(app, db)
    
    # configure routes
    app.register_blueprint(home_routes)
    app.register_blueprint(book_routes)
    
    return app

if __name__ == "__main__":
    web_app = create_app()
    web_app.run(debug=True)
    
#FLASK_APP=web_app flask db migrate #> creates the db (with "alembic_version" table)
#FLASK_APP=web_app flask db upgrade #> creates the specified tables