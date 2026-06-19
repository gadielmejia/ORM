from flask import Flask
from flask_migrate import Migrate
from app.config.settings import Config
from app.database.database import db,bcrypt

migrate= Migrate()

import app.models

def create_app():
    
    app = Flask(__name__)
    
    app.config.from_object(Config)
    
    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)
    
    return app