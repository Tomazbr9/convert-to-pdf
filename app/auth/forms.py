from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, SubmitField

from wtforms.validators import DataRequired, Length

class AuthForm(FlaskForm):
    username = StringField(
        'Nome de Usuário', validators=[DataRequired(), Length(min=2, max=50)]
    )

    password = PasswordField(
        'Senha', validators=[DataRequired(), Length(min=6)]
    )