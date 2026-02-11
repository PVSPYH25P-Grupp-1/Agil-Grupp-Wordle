import random
from flask import Flask, json, render_template

from models.forms import WordleGuesses
from validation import validate

app = Flask(__name__)
app.config["SECRET_KEY"] = 'SECRET_KEY_NON_ENV_FIX_LATER'

with open("data/answer.json") as f:
    words = json.load(f)["words"]

answer=random.choice(words)
guesses=[]
print("ANSWER:",answer)


@app.route("/", methods=["GET", "POST"])
def main():
    form = WordleGuesses()
    print(guesses)
    if form.guess.data is not None:
        guesses.append(validate(answer,form.guess.data))
        form.guess.data = None
    return render_template('wordle/wordle_guess.html', form=form, guesses=guesses)

@app.route('/wordle')
def wordle():
    pass

if __name__ == '__main__':
    app.run(debug=True)