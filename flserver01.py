from flask import Flask

app = Flask(__name__)

@app.route('/')     # controller
def index():
    return 'Hello Flask!'


if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = 8080)
