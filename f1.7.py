# 1. 모듈 가져오기
from flask import Flask, request, render_template

# 2. 앱 생성(서버 생성)
app = Flask(__name__)

# 3. 라우팅(요청을 분석하여 어떤 함수가 응답할지 매칭)
@app.route('/')
def home(): 
    # 보여주고자 하는 html을 만들어서 templates폴더 밑에 위치
    # render_template('html 파일명')
    # => html을 랜더링해서 뿌려준다
    # 응답
    return render_template('login.html', name='멀티')

@app.route('/login')
def login():
    uid = request.args.get('uid')
    upw = request.args.get('upw')

    if uid == 'test' and upw == '1234':
        return '회원입니다'
    else:
        return '''
        <script>
            alert("%s");     //팝업 띄우기
            history.back();  //이전 페이지 이동
        </script>
        ''' % '일치하는 회원정보가 없습니다. 가입하겠습니까?'

# 4. 서버 가동
if __name__ == '__main__':
    app.run(debug = True)
else:
    print('본 모듈은 단독으로 구동될 때만 정상 작동합니다')