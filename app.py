import random
from flask import Flask, json, render_template

# from models.forms import WordleGuesses

app = Flask(__name__)
app.config["SECRET_KEY"] = 'SECRET_KEY_NON_ENV_FIX_LATER'

with open("data/allow_words.json") as f:
    allow_words = set(json.load(f)["words"])

answer=random.choice(list(allow_words))
guesses=[]
print("ANSWER:",answer)

def validate(currentWord, userGuess):
    result = []
    word = list(currentWord.lower())
    guess = list(userGuess.lower())
    count = 0
    for letter in guess:
        if letter == word[count]:
            result.append('O')
        elif letter in word:
            result.append('?')
        else:
            result.append('x')
        count += 1
    return result

@app.route("/")
def main():
    return render_template(
        "index.html",
        answer=answer,
        words=sorted(list(allow_words))
    )

@app.route('/wordle', methods=["GET", "POST"])
def wordle():
    return render_template('wordle/wordle_guess.html', guesses=guesses)

if __name__ == '__main__':
    app.run(debug=True)