flask run 으로 실행하지만 그를 위한 준비사항

1. SET FLASK_APP=main/__init__.py

error

Error: Could not locate a Flask application. You did not provide the "FLASK_APP" environment variable, and a "wsgi.py" or "app.py" module was not found in the current directory.
그런데 로컬 서버를 실행하면 "플라스크 애플리케이션을 찾을 수 없다"는 오류가 발생한다. 오류 메시지를 조금 더 자세히 보면 "FLASK_APP 환경 변수가 없다"라고 표시되어 있다. 즉, 플라스크 서버를 실행하려면 반드시 FLASK_APP 환경 변수에 플라스크 애플리케이션을 설정해야 한다.


FLASK_APP 환경 변수의 기본값

플라스크는 FLASK_APP 환경 변수가 지정되지 않은 경우 자동으로 app.py 파일을 기본 애플리케이션으로 인식한다. 따라서 앞의 pybo.py 파일을 app.py로 만들었다면 FLASK_APP 환경 변수를 별도로 지정하지 않아도 된다. 하지만 우리는 FLASK_APP 환경 변수의 값을 수정하여 이 문제를 해결할 것이다.

set FLASK_ENV=development


python main/__init__.py 또는 (mgs_flask) C:\Users\GreatChoi\Documents\D_DriveBackup\ajisweb\마제스티\Magesty\venv\app>flask run

참고:
[1] https://codechacha.com/ko/how-to-import-python-files/

