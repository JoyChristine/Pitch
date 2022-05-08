from wtforms import TextAreaField,SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [DataRequired()])
    submit = SubmitField('Submit')