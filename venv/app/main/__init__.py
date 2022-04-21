#상위 경로를 import 하기 위에서 아래 sys를 통해서 경로를 받아온다.
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from models.model import db 
import config
#from config import user, pwd, host, database, port  # 데이터베이스 기본 정보 입력

#from model import db
# 현재있는 파일의 디렉토리 절대경로
basdir = os.path.abspath(os.path.dirname(__file__))
# basdir 경로안에 DB파일 만들기
dbfile = os.path.join(basdir, 'db.sqlite')

db = SQLAlchemy()
migrate = Migrate()

# 내가 사용 할 DB URI

#app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s"
#app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#db = SQLAlchemy(app)
#
#print(db)



#블루프린트 라우팅 부분을 구현하기 위한 함수
#views -> main_views.py로 보내는 함수
def create_app():
    app = Flask(__name__)
    # SQLAlchemy 설정
    app.config.from_object(config)
    
    # ORM
    db.init_app(app)
    migrate.init_app(app, db)


   # # 내가 사용 할 DB URI
   # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
   # # 비지니스 로직이 끝날때 Commit 실행(DB반영)
   # app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
   # # 수정사항에 대한 TRACK
   # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
   # # SECRET_KEY
   # app.config['SECRET_KEY'] = 'jqiowejrojzxcovnklqnweiorjqwoijroi'
    
    #sqllite 데이터 베이스 생성 파트
    #db.init_app(app)
    #db.app = app
    #db.create_all()
    
    from views import main_views
    app.register_blueprint(main_views.bp)
    
    return app




# 현재있는 파일의 디렉토리 절대경로
# basdir = os.path.abspath(os.path.dirname(__file__))
# basdir 경로안에 DB파일 만들기
# dbfile = os.path.join(basdir, 'db.sqlite')

# config.py 설정파일

# app.config.from_object('config')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# SECRET_KEY
# app.config['SECRET_KEY'] = 'jqiowejrojzxcovnklqnweiorjqwoijroi'
# db = SQLAlchemy(app)
# migrate = Migrate(app, db) # ORM을 적용하기 위해선 migration이 필요하다.

# db.init_app(app)
# db.app = app
# db.create_all()


#if __name__ == '__main__':
#    app.run(host='0.0.0.0', port=8073, debug=True)

