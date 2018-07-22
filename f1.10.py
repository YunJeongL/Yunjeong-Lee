# 1. 모듈 가져오기
from flask import Flask, request, render_template, redirect, url_for

# # 2. 앱 생성(서버 생성)
app = Flask(__name__)

# 3. 라우팅(요청을 분석하여 어떤 함수가 응답할지 매칭)
# 하나의 주소(URL)에 get, post를 다 받아서 내부에서 나눠서 처리하게 하는 방법 
# 하나의 주소에서 get, post와 같이 다양한 메소드를 지원하여 마치 여러 개의 페이지(주소)가 존재하도록 처리하는 방식

# restful(레스트풀)
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        # 응답
        return render_template('login.html', name='test')
    else:  # elif request.method == 'POST'  # POST
        # 응답, 로그인 실제 처리(디비연동)
        #return 'login process'
        return loginProcess()

# 별도의 함수로 처리 루틴을 빼도 관계없음
def loginProcess():
    # 아이디 비번 획득
    uid = request.form['uid']
    upw = request.form['upw']
    print(uid,upw)
    # 디비 쿼리 수행
    if uid == '1' and upw =='1':
        # 회원일 때 처리 -> 메인 서비스로 이동 -> 포워딩
        # 포워딩 : 요청에 응답하지 않고, 요청을 다른 주소로 이어주는 방법
        # url_for('특정 url과 연결된 함수명')
        # url_for('main') => '/service'
        return redirect(url_for('main'))
        #return redirect('/main')
        #return render_template('alert2.html', msg='로그인성공', url='/main')
    else:
        # 회원아닐 때 처리 -> 경고창 -> 되돌아가기
        return render_template('alert.html', msg='회원아님')
    # return 'login process'

# 지금은 그냥 이 페이지를 진입할 수 있으나,
# 향후 세션(session)을 이용하여 로그인 후에만 접근할 수 있게 제한할 것이다
@app.route('/service')
def main():
    return 'main page' 

# 4. 서버 가동
if __name__ == '__main__':
    app.run(debug=True)