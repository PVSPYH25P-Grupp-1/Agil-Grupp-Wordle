from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SubmitField
)
from wtforms.validators import DataRequired, Length

class WordleGuesses(FlaskForm):
    guess = StringField(
        validators=[Length(min=5, max=5), DataRequired()],
    )
    submit = SubmitField("Confirm")