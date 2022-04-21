import sys
import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models.model import db    # 아래에서 작성
from config import user, pwd, host, database, port  # 데이터베이스 기본 정보 입력
#from model import db

# 현재있는 파일의 디렉토리 절대경로
basdir = os.path.abspath(os.path.dirname(__file__))
# basdir 경로안에 DB파일 만들기
dbfile = os.path.join(basdir, 'db.sqlite')

app = Flask(__name__)
# SQLAlchemy 설정
# 내가 사용 할 DB URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
# 비지니스 로직이 끝날때 Commit 실행(DB반영)
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# 수정사항에 대한 TRACK
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# SECRET_KEY
app.config['SECRET_KEY'] = 'jqiowejrojzxcovnklqnweiorjqwoijroi'

# 내가 사용 할 DB URI

#app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s"
#app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#db = SQLAlchemy(app)
#
#print(db)

#mysql.init_app(app)
db.init_app(app)
db.app = app
db.create_all()

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        id = request.form['login_id']
        pw = request.form['login_pw']
 
        conn = db.connect()
        cursor = conn.cursor()
 
        sql = "SELECT * FROM a_MagestyMember where id='%s' and pwd='%s')" % (id, pw)
        cursor.execute(sql)
        print(sql)
        data = cursor.fetchall()
 
        if not data:
            conn.commit()
            return redirect(url_for('login'))
        else:
            conn.rollback()
            return "Register Failed"
 
        cursor.close()
        conn.close()
        return render_template("login.html")


@app.route('/register')
def register():
    error = None
    return render_template('register.html')


@app.route('/dashboard')
def dashboard():
    error = None
    return render_template('dashboard.html')

@app.route('/admin')
def adiministrator():
    error = None
    return render_template('administrator.html')

@app.route('/gendatview')
def gendatview():
    error = None
    return render_template('administrator.html')

@app.route('/main')
def main():
    error = None
    if request.method == 'POST':
        id = request.form['id']
        pw = request.form['pw']
 
        conn = mysql.connect()
        cursor = conn.cursor()
        sql = "SELECT id FROM users WHERE id = %s AND pw = %s"
        value = (id, pw)
        cursor.execute("set names utf8")
        cursor.execute(sql, value)
 
        data = cursor.fetchall()
        cursor.close()
        conn.close()
 
        for row in data:
            data = row[0]
            print(row[0])

        if data:
            session['login_user'] = id
            return redirect(url_for('home'))
        else:
            error = 'invalid input data detected !'
    return render_template('main.html', error = error)


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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8073, debug=True)

