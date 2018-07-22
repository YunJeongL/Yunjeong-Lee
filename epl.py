from flask import Flask, render_template, redirect, url_for, session, request, jsonify, make_response
from service.controller import bp_epl as app
# 디비
from service.model import dbHelper
from service import config

# eplList
# ~/epl/eplList
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
    rows = dbHelper.selectAllEplList(page=page*amt)
    # 화면처리
    return render_template('eplList.html', config=config, epls=rows)

# 검색 결과
# ~/epl/search
@app.route('/search', methods=['POST'])
def search():
    keyword = request.form['keyword']
    tmp = dbHelper.searchSql(keyword)
    if tmp == None: tmp=[]
    return jsonify(tmp)
