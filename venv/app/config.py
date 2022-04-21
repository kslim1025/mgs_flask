import os
BASE_DIR = os.path.dirname(__file__)
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'dbsplite.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Database parameter
host = "211.117.60.37"         
user = "ajis"          
pwd = "@jis2021!"    
database = "magesty"
port = "1433"    



























#from sqlalchemy import create_engine, Table, Column, Integer, String, DateTime, Float, MetaData
#import pymssql

# pip install pymysql
# Database parameter
#host = "211.117.60.37"         
#user = "ajis"          
#password = "@jis2021!"    
#database = "magesty"
#port = "1433"    

# Database connection
#db=pymssql.connect(
#        host=host,
#        user=user,
#        password=password,
#        database=database,
#        autocommit=True)

# pymssql
#engine = create_engine('mssql+pymssql://{user}:{password}@{host}/{database}')
#cursor=db.cursor()
#print(cursor)