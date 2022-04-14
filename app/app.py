import sys
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# config.py 설정파일
app.config.from_object('config')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.secret_key = 'flasknotewithsqlalchemy'
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template("index.html")

if __name__=='__main__':
    app.run(debug=True)