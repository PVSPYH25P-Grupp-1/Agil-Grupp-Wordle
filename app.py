import random
from flask import Flask, json, render_template

from models.forms import WordleGuesses
from validation import validate, check_guess_validity

app = Flask(__name__)
app.config["SECRET_KEY"] = 'SECRET_KEY_NON_ENV_FIX_LATER'

with open("data/allow_words.json") as f:
    words = json.load(f)["words"]

answer=random.choice(words)
guesses=[]
print("ANSWER:",answer)


@app.route("/", methods=["GET", "POST"])
def main():
    form = WordleGuesses()

    if form.guess.data is not None and check_guess_validity(form.guess.data, words)[0] != False:
        guesses.append(validate(answer,form.guess.data))
        form.guess.data = None
    else:
        form.guess.data = "Invalid Word"
    return render_template('wordle/wordle_guess.html', form=form, guesses=guesses)

@app.route('/wordle')
def wordle():
    pass

if __name__ == '__main__':
    app.run(debug=True)