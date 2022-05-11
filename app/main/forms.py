from wtforms import TextAreaField,SubmitField,SelectField
from wtforms.validators import InputRequired
from flask_wtf import FlaskForm



class UpdateProfile(FlaskForm):
    bio = TextAreaField('Write something about yourself',validators = [InputRequired()])
    submit = SubmitField('Submit')

class PitchForm(FlaskForm):
    category = SelectField('Pitch category',choices=[('Interview','Interview'),('Product','Product'),('Promotion','Promotion'),('Business','Business')],validators = [InputRequired()])
    pitch_title = TextAreaField('Pitch title',validators = [InputRequired()])
    content = TextAreaField('Pitch content',validators = [InputRequired()])
    
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('What do you think?',validators = [InputRequired()])
    submit = SubmitField('Submit')