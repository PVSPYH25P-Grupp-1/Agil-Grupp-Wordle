# add code later...


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('main/index.html')


@app.route('/wordle')
def game():
    return render_template('wordle/index.html')

if __name__ == '__main__':
    app.run(debug=True)