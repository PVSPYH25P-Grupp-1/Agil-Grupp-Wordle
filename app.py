import random
from flask import Flask, json, render_template


app = Flask(__name__)

with open("data/answer.json") as f:
    words = json.load(f)["words"]

answer=random.choice(words)
print("ANSWER:",answer)

@app.route("/")
def main():
    answer = random.choice(words)
    return render_template(
        "wordle_guess.html",
        answer=answer,
        words=words
    )

@app.route('/wordle')
def game():
    return render_template('wordle/wordle_guess.html')

if __name__ == '__main__':
    app.run(debug=True)