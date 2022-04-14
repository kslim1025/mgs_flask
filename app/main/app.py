# pip list > requirements.txt
# 필요한 패키지 목록

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'sibal'

if __name__=='__main__':
    app.run(debug=True)