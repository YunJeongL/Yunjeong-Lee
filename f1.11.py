# 1. 모듈 가져오기
from flask import Flask, request, render_template, redirect, url_for
from d1_8 import loginSql

# 2. 앱 생성(서버 생성)
app = Flask(__name__)

# 3. 라우팅(요청을 분석하여 어떤 함수가 응답할지 매칭)
# restful(레스트풀)
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html', name='test')
    else:  # POST
        return loginProcess()

# 별도의 함수로 처리 루틴을 빼도 관계없음
def loginProcess():
    # 아이디 비번 획득
    uid = request.form['uid']
    upw = request.form['upw']
    print(uid,upw)
    # 디비 쿼리 수행
    rows = loginSql(uid, upw)
    if rows :  # uid == '1' and upw =='1':
        # ~/service?name=멀티
        # 회원정보를 포워딩할 때 get방식에 맞춰서 전달
        return redirect(url_for('main') + '?name=%s' % rows[0]['name'])
    else:
        return render_template('alert.html', msg='회원아님')

@app.route('/service')
def main():
    return 'main page %s' % request.args.get('name') 

# 4. 서버 가동
if __name__ == '__main__':
    app.run(debug=True)