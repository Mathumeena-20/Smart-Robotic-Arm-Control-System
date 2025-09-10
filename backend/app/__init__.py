from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from .config import Config # ✅ FIXED IMPORT

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config) 
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:mysecretpassword@db:5432/robotics"

    CORS(app)

    db.init_app(app)
    migrate.init_app(app, db)

    # Import and register Blueprints here if needed
    # from .routes import some_blueprint
    # app.register_blueprint(some_blueprint)

    return app
