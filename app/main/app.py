# pip list > requirements.txt
# 필요한 패키지 목록

from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return '''
    <DOCTYPE html>
    <head>
    <title>Magesty</title>
    </head>
    <body>
    <p>간단한 테스트</p>
    </body>
    </html>
    '''

@app.route('/user')
def user():
    return 'hello'

if __name__=='__main__':
    app.run(debug=True)