from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
     """Application-factory pattern"""
     db.init_app(app)
     migrate.init_app(app, db)
     return app