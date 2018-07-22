from flask import Flask, render_template, redirect, url_for, session, request, jsonify
# 환경설정 클래스 모듈 가져오기
from service.config import WebConfig
from service.model.dbMgr import loginSql, searchSql, selectAllEplList

app = Flask(__name__)
# 세션생성에 필요한 세션키(중복되지 않는 해쉬값)를 정의
app.secret_key = 'dlghkdhlrh'
config = WebConfig()

# 세션이 없어도 접근 가능한 페이지는 오직 로그인
# 세션생성, 세션종료, 세션체크
@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html',config=config)
    else:
        uid = request.form['uid']
        upw = request.form['upw']
        row = loginSql(uid, upw)
        # if false : [], (), {}, 0, ""
        # row => dict => {}
        if row : 
            # 세션처리(필요한 정보를 세션으로 저장한다)
            # 사용자 아이디와 이름 저장하겠다
            session['uid'] = uid
            session['name'] = row['name']
            return redirect(url_for('home'))
        else:
            return render_template('common/alert2.html', msg='회원아님')

# 홈페이지
@app.route('/')
def home():
    # 세션이 없으면 /login으로 리다이렉트
    if not 'uid' in session:  # 세션 없으면 false -> 부정 -> 참
        return redirect(url_for('login'))
    ###########################################################   
    return render_template('index.html', config = config)

# 로그아웃
@app.route('/logout')
def logout():
    if not 'uid' in session:  # 세션 없으면 false -> 부정 -> 참
        return redirect(url_for('login'))
    # 세션 종료
    print(session)

    if 'uid' in session:
        session.pop('uid', None)
    if 'name' in session:
        session.pop('name', None)

    print('세션제거후->', session)
  
    # 페이지 요청을 리다이렉트 -> 홈페이지
    return redirect(url_for('home'))

# eplList
@app.route('/eplList')
def eplList():
    # 세션체크
    #if not 'uid' in session:  # 세션 없으면 false -> 부정 -> 참
    #    return redirect(url_for('login'))
    # 데이터 획득
    amt = 5;  # 한번에 보여줄 양(한페이지에 5개 보여줌)
    tmp = request.args.get('page')
    page = 0  # 최종 페이지값 초기값
    if tmp:  # 전달된 페이지가 있다면(인자값이 전달되면 참) ex) eplList?page=2,...
        # 페이지 계산 2로 전달되면 1로 계산해야함(쿼리기준)
        page = int(tmp) - 1 ;
    # 최종 결과 획득    
    rows = selectAllEplList(page=page*amt)
    # 화면처리
    return render_template('eplList.html', config=config, epls=rows)

# 검색결과
@app.route('/search', methods=['POST'])
def search():
    keyword = request.form['keyword']
    tmp = searchSql(keyword)
    if tmp == None: tmp=[]
    return jsonify(tmp)


if __name__ == '__main__':
    app.run(debug=config.debug)