from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Pyservice', 200


@app.route('/<name>')
def user_name(name):
    return 'Hello ' + name


if __name__ == '__main__':
    app.run()