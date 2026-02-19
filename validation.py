

from typing import Literal, Set, Tuple


def validate(currentWord, userGuess):
    result = []
    word = list(currentWord.lower())
    guess = list(userGuess.lower())
    count = 0
    for letter in guess:
        if letter == word[count]:
            result.append([letter, 'green'])
        elif letter in word:
            result.append([letter, 'yellow'])
        else:
            result.append([letter, 'red'])
        count += 1
    return result

def check_guess_validity(user_guess: str, allowed_word:Set[str]) -> Tuple[bool,str]:
    guess = (user_guess or"").strip().lower()
    
    #length check
    if len(guess)!=5:
        return False, "Guess must be 5 letter."
    
    #word list check
    if guess not in allowed_word:
        return False, "Not in word list."
    return True, ""