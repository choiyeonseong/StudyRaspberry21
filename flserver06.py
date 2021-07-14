from flask import Flask, render_template, request

# Flask 객체 인스턴스 생성
app = Flask(__name__)

@app.route('/')  # 접속하는 최초 url
def index():
    # 백엔드에서 데이터를 프론트엔드로 전달
    return render_template('login.html')  # post
    # return render_template('index.html') # get

@app.route('/get', methods=['GET']) # GET : url에 정보 다 표시, 다른 서버를 요청할때
def get():
    user = request.args.get('user')
    msg = "{0}".format(user)

    # 백엔드에서 데이터를 프론트엔드로 전달
    return msg

@app.route('/post', methods=['POST']) # POST : 숨기기, 내서버에서 호출할때
def post():
    userid = request.form.get('userid')
    password = request.form.get('password')
    msg = "{0} / {1}".format(userid, password)
    friends = ['Lee', 'Park', 'Kim']

    # 백엔드에서 데이터를 프론트엔드로 전달
    return render_template('result.html', result=msg, friends=friends)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)    # 디버깅하기 위해 debug값 추가
