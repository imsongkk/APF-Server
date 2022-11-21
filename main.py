from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/pose', methods=['POST'])
def pose():
    params = request.get_json()
    return ''


if __name__ == '__main__':
    app.run(host='0.0.0.0')
