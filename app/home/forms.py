from flask_wtf import FlaskForm

from flask_wtf.file import FileField, FileRequired, FileAllowed

class FileForm(FlaskForm):
    file = FileField(
        'Escolha o arquivo', 
        validators=[
            FileRequired(),
            FileAllowed(['txt', 'docx', 'doc', 'rtf', 'html', 'ods', 'xls', 'xlsx', 'csv', 'odp', 'ppt', 'pptx', 'odg', 'svg', 'png', 'jpg', 'bmp'], 'Formato não suportado para conversão')
        ]
    )
    