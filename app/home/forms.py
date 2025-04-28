from flask_wtf import FlaskForm

from wtforms import SubmitField, URLField

from wtforms.validators import DataRequired

class FileForm(FlaskForm):
    file = URLField('File', validators=[DataRequired()])
    
    submit = SubmitField('Converter')