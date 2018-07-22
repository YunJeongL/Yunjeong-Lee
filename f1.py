# -*- coding: utf-8 -*-
# 1. 모듈 가져오기
from flask import Flask

# # 2. 앱 생성(서버 생성)
app = Flask(__name__)

# 3. 라우팅(요청을 분석하여 어떤 함수가 응답할지 매칭)
@app.route('/')
def home():
    return 'Home Page'

# 4. 서버 가동
if __name__ == '__main__':
    app.run(debug=True)