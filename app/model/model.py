from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'a_MagestyMember'
    sort = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id = db.Column(db.String(50))
    email = db.Column(db.String(50))
    pwd = db.Column(db.String(128))  

class UserRegist(db.Model):
    __tablename__= 'a_MagestyMember'
    sort = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id = = db.Column(db.String(50))
    group_cd = db.Column(db.String(50))
    sex_fg = db.Column(db.String(2))
    name = db.Column(db.String(50))
    add1 = db.Column(db.String(150))
    tel_no2 = db.Column(db.String(150))
    email = db.Column(db.String(50))
    pwd = db.Column(db.String(128)) 
   