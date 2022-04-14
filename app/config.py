from sqlalchemy import create_engine, Table, Column, Integer, String, DateTime, Float, MetaData
import pymssql

# pip install pymysql
# Database parameter
host = "211.117.60.37"         
user = "ajis"          
password = "@jis2021!"    
database = "ajis"     

# Database connection
db=pymssql.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        autocommit=True)

# pymssql
#engine = create_engine('mssql+pymssql://{user}:{password}@{host}/{database}')
cursor=db.cursor()
print(cursor)