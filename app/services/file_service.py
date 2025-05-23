from flask import current_app

from flask_login import current_user

from app.converters.convert_to_pdf import convert_to_pdf, convert_img_to_pdf

from app.models.file import FileModel

from werkzeug.utils import secure_filename

from app import db

import os

import tempfile

def get_output_path(original_name: str) -> str:
    # gera caminho seguro para salvar o PDF na pasta 'media'
    safe_filename = original_name.replace(' ', '_')
    media_path = os.path.join(current_app.root_path, 'media')
    os.makedirs(media_path, exist_ok=True)  # garante que diretório existe
    output_path = os.path.join(media_path, f'{safe_filename}.pdf')
    return output_path

def save_temp_file(file):
    temp_dir = tempfile.mkdtemp()  # cria diretório temporário único
    temp_path = os.path.join(temp_dir, secure_filename(file.filename))
    file.save(temp_path)
    return temp_path


def save_file_in_database(output_path: str, user_id: int):
    file_record = FileModel(
        filename=os.path.basename(output_path), # type:ignore  # salva apenas o nome do arquivo, não caminho completo
        filepath=output_path, # type:ignore
        filesize=os.path.getsize(output_path), # type:ignore
        user_id=user_id # type:ignore
    )

    db.session.add(file_record)
    db.session.commit()

    return file_record

def save_converted_file(file) -> FileModel:
    original_name = os.path.splitext(file.filename)[0]
    original_ext = os.path.splitext(file.filename)[1].lower()
    
    output_path = get_output_path(original_name)
    temp_path = save_temp_file(file)
    
    # escolhe função de conversão conforme o tipo do arquivo
    if original_ext in ['.txt', '.docx', '.doc', '.rtf', '.html', '.ods', '.xls', '.xlsx', '.csv', '.odp', '.ppt', '.pptx', '.odg', '.svg']:
        convert_to_pdf(temp_path, output_path)
    elif original_ext in ['.png', '.jpg', '.bmp']:
        convert_img_to_pdf(temp_path, output_path)
    else:
        raise ValueError('Tipo de arquivo não suportado para conversão')
    
    if current_user.is_authenticated:
        file_record = save_file_in_database(output_path, current_user.id)

    return file_record
