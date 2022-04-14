# pip list > requirements.txt
# 필요한 패키지 목록

from flask import Flask
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("login.html")



if __name__=='__main__':
    app.run(debug=True)