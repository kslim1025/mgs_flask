from flask import Blueprint
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def home():
    return 'sibal'
    #return render_template("index.html")

@bp.route('/login', methods=['GET', 'POST'])
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


@bp.route('/register')
def register():
    error = None
    return render_template('register.html')


@bp.route('/dashboard')
def dashboard():
    error = None
    return render_template('dashboard.html')

@bp.route('/admin')
def adiministrator():
    error = None
    return render_template('administrator.html')

@bp.route('/gendatview')
def gendatview():
    error = None
    return render_template('administrator.html')

@bp.route('/main')
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
