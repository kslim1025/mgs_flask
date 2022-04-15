from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'a_MagestyMember'
    
    sort = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.String(50))
    email = db.Column(db.String(50))
    pwd = db.Column(db.String(128))  