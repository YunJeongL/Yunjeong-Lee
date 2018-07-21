# 1. 모듈 가져오기
from flask import Flask, request, render_template

# # 2. 앱 생성(서버 생성)
app = Flask(__name__)

# 3. 라우팅(요청을 분석하여 어떤 함수가 응답할지 매칭)
# 데코레이터는 하나의 함수에 여러 개를 연결할 수 있다
# @~ : 데코레이터
# ~/ or ~/pp
@app.route('/test')  # 내부적으로 이렇게 호출 : home()
@app.route('/test/<id>')  # 내부적으로 이렇게 호출 : home('pp')
def home(id=None):
    if id:
        return 'sub page %s' %id
    else:
        return 'home page'


# 4. 서버 가동
if __name__ == '__main__':
    app.run(debug=True)