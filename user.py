from flask import Flask, render_template, redirect, url_for, session, request, jsonify, make_response
from service.controller import bp_user as app
# 디비
from service.model import dbHelper
from service import config

# 라우팅
# 홈페이지
# ~/user
@app.route('/')
def home():
    # 세션이 없으면 /login으로 리다이렉트
    # if not 'uid' in session:  # 세션 없으면 false -> 부정 -> 참
    #    return redirect(url_for('login'))
    ###########################################################   
    # 쿠키 적용 -> 아이디를 저장해서 로그인 페이지 뜰 때 자동으로 아이디가 보이게 처리
    # 응답 객체를 생성한다
    resp = make_response(render_template('index.html', config = config))
    # 쿠키 세팅
    resp.set_cookie('uid', session['uid'])
    return resp

# ~/user/login
@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'GET':
        # 쿠키 획득
        uid = request.cookies.get('uid')
        # 쿠키가 없을 경우 : None으로 나오기 때문에 기본값 처리
        if not uid:  # if uid == None:
            uid=''
        config.cookie_uid = uid
        return render_template('login.html',config=config)
    else:
        uid = request.form['uid']
        upw = request.form['upw']
        row = dbHelper.loginSql(uid, upw)
        # if false : [], (), {}, 0, ""
        # row => dict => {}
        if row : 
            # 세션처리(필요한 정보를 세션으로 저장한다)
            # 사용자 아이디와 이름 저장하겠다
            session['uid'] = uid
            session['name'] = row['name']
            return redirect(url_for('userbp.home'))
        else:
            return render_template('common/alert2.html', msg='회원아님')

# 로그아웃
# ~/user/logout
@app.route('/logout')
def logout():
    if not 'uid' in session:  # 세션 없으면 false -> 부정 -> 참
        return redirect(url_for('userbp.login'))
    # 세션 종료
    print(session)

    if 'uid' in session:
        session.pop('uid', None)
    if 'name' in session:
        session.pop('name', None)

    print('세션제거후->', session)

    # 페이지 요청을 리다이렉트 -> 홈페이지
    return redirect(url_for('userbp.home'))
