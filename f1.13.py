# # ~/add/<x>/<y> -> 리다이렉트 -> ~/mul?res=xxx -> 리다이렉트 -> ~/show/<value>
# add 페이지는 x + y
# mul 페이지는 res*10 던져준다
# show 최종값을 보여준다
from flask import Flask, url_for, redirect, request

app = Flask(__name__)

# get 방식
@app.route('/add/<int:x>/<int:y>')
def add(x,y):
    sum = x + y
    #return redirect('/mul?res=sum값')
    return redirect('%s?res=%s' %(url_for('mul'), sum))

@app.route('/mul')
def mul():
    sum = int(request.args.get('res')) * 10
    return redirect(url_for('show', value=sum))

@app.route('/show/<value>')
def show(value):
    return '최종값 = ' + value 

if __name__ == '__main__':
    app.run(debug=True)