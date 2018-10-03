from flask import Flask

app = Flask(__name__)


@app.route('/python')
def hello_world(name):
    return 'Your name is: {}'.format(name)




if __name__ == '__main__':
    app.run()
