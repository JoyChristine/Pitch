from wtforms import TextAreaField,SubmitField
from wtforms.validators import InputRequired
from flask_wtf import FlaskForm



class UpdateProfile(FlaskForm):
    bio = TextAreaField('Write something about yourself',validators = [InputRequired()])
    submit = SubmitField('Submit')

class PitchForm(FlaskForm):
    pitch_title = TextAreaField('Pitch title',validators = [InputRequired()])
    content = TextAreaField('Pitch content',validators = [InputRequired()])
    category = TextAreaField('Pitch category',validators = [InputRequired()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('Any Comment',validators = [InputRequired()])
    submit = SubmitField('Submit')