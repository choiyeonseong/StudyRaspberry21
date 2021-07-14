from flask import Flask, render_template, request
import MySQLdb as mysql

# Flask 객체 인스턴스 생성
app = Flask(__name__)

@app.route('/')  # 접속하는 최초 url
def index():
    db = mysql.connect('localhost', 'root', '12345', 'test', charset='utf8')
    cur = db.cursor(mysql.cursors.DictCursor)
    cur.execute('SELECT * FROM student')
    result = []
    while True:
        student = cur.fetchone()
        if not student: break

        result.append(student)  # 리스트 추가
        
    cur.close()
    db.close()

    # 백엔드에서 프론트엔드로 row 데이터 전달
    return render_template('mysqldata.html', row = result)  
   

if __name__ == '__main__':
    app.run(host='192.168.0.9', port=8080, debug=True)    # 디버깅하기 위해 debug값 추가
