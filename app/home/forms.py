from flask_wtf import FlaskForm

from flask_wtf.file import FileField, FileRequired, FileAllowed

class FileForm(FlaskForm):
    file = FileField(
        'Escolha o arquivo', 
        validators=[
            FileRequired(),
            FileAllowed(['txt'], 'Formato não suportado para conversão')
        ]
    )
    