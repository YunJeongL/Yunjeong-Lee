# 클라이언트가 웹페이지를 요청할 때 데이터를 보내고 싶다
# 대표적인 케이스 => 검색, 로그인, 링크클릭 등...
# 데이터를 보내는 방법 : method(get, post, put, delete,...), 동적파라미터
# 데이터를 가지고 페이지를 요청하는 방법 중 : 동적 파라미터
# 1. 모듈 가져오기
from flask import Flask

# 2. 앱 생성(서버 생성)
app = Flask(__name__)

# 3. 라우팅(요청을 분석하여 어떤 함수가 응답할지 매칭)
# 요청: http + :// + 아이피 + : + 포트 + / + 세부페이지이름
@app.route('/')
def home():
    return 'home page'

# 동적 파라미터 1 => URL(주소)에 데이터를 보내는 방법
@app.route('/news/<news_id>')
def news(news_id):
    return '전달된 데이터 %s' %news_id

# 전달된 데이터가 보이면 안되는 것(아이디, 비번 등...)
# 이런 데이터는 전달하면 안된다 -> 보안에 취약하다
@app.route('/login/<uid>/<upw>')
def login(uid,upw):
    return '%s %s' %(uid,upw)

# 동적 파라미터 2 : 타입을 지정하여 보다 명확하게 데이터를 전달할 수 있다
# 타입 : int(정수), float(부동소수,소수), path(가변경로)
@app.route('/test/<int:num>')
def test(num):
    return '정수형 전달 데이터 %s' %num 

@app.route('/test2/<path:num>')
def test2(num):
    # 전달 데이터 분해해서 표시하기
    return '전달 데이터 %s' %num.split('/')     

# 4. 서버 가동
if __name__ == '__main__':
    app.debug = True
    app.run()
else:
    print('본 모듈은 단독으로 구동될 때만 정상 작동합니다')