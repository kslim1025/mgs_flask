import sys
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
#from model import db    # 아래에서 작성
from config import user, password, host, database, port #데이터베이스 기본 정보 입력

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("login.html")

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/admin')
def adiministrator():
    return render_template('administrator.html')


# 현재있는 파일의 디렉토리 절대경로
#basdir = os.path.abspath(os.path.dirname(__file__))
# basdir 경로안에 DB파일 만들기
#dbfile = os.path.join(basdir, 'db.sqlite')

# config.py 설정파일

#app.config.from_object('config')
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# SECRET_KEY
#app.config['SECRET_KEY'] = 'jqiowejrojzxcovnklqnweiorjqwoijroi'
#db = SQLAlchemy(app)
#migrate = Migrate(app, db) # ORM을 적용하기 위해선 migration이 필요하다.

#db.init_app(app)
#db.app = app
#db.create_all()


if __name__=='__main__':
    app.run(host='0.0.0.0', port=8073,debug=True)

    