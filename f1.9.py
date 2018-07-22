# 1. 모듈 가져오기
from flask import Flask, request, render_template

# # 2. 앱 생성(서버 생성)
app = Flask(__name__)

# 3. 라우팅(요청을 분석하여 어떤 함수가 응답할지 매칭)

@app.route('/')  # 내부적으로 이렇게 호출 : home()
def home():
    teams = [ {'rank':1, 'team':'프랑스'},
    {'rank':2, 'team':'벨기에'},
    {'rank':3, 'team':'잉글랜드'},
    {'rank':4, 'team':'크로아티아'} ]
    # teams 안의 팀을 하나씩 출력하시오
    for team in teams:
        # 랭킹하고 팀명을 출력하시오 -> 인덱싱(indexing) : 변수명[키]
        print(team['rank'], team['team'])
        
    # 응답
    return render_template('index.html', title='제목', fourTeams=teams)

# 4. 서버 가동
if __name__ == '__main__':
    app.run(debug=True)