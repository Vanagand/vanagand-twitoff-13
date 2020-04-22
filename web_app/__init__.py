# web_app/__init__.py
# $env:FLASK_APP = "web_app" > flask run

from flask import Flask
from web_app.models import db, migrate

from web_app.routes.home_routes import home_routes
from web_app.routes.book_routes import book_routes

# application factory pattern
def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////Users/Michel/Desktop/lambda_ds13/vanagand-twitoff-13/web_app/twitoff_13.db"
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    app.register_blueprint(home_routes)
    app.register_blueprint(book_routes)
    
    return app

if __name__ == "__main__":
    web_app = create_app()
    web_app.run(debug=True)
    