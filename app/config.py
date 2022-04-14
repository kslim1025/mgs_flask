from sqlalchemy import create_engine

#MSSQL 연동
#engine = create_engine('mssql+pymsql://username:passwd@host/database',echo=True)
engine = create_engine('mssql+pymsql://ajis:@jis2021!@211.117.60.37/magesty',echo=True)