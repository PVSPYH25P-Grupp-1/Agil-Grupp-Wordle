# add code later...


from flask import Flask

app = Flask(__name__)


@app.route('/')
def main():
    return ''


@app.route('/game')
def game():
    return ''

if __name__ == '__main__':
    app.run(debug=True)