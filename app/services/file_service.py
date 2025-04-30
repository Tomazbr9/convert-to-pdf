from flask import current_app

from app.converters.pdf_from_text import text_to_pdf
from app.converters.pdf_from_doc import doc_to_pdf

from werkzeug.utils import secure_filename

from app.models.file import FileModel

import os

from app import db

import tempfile

def get_output_path(original_name: str) -> str:
    media_path = os.path.join(current_app.root_path, 'media')
    os.makedirs(media_path, exist_ok=True)
    output_path = os.path.join(media_path, f'{original_name}.pdf')
    return output_path

def save_temp_file(file):
    temp_dir = tempfile.mkdtemp()
    temp_path = os.path.join(temp_dir, secure_filename(file.filename))
    file.save(temp_path)
    return temp_path

def save_file_in_database(output_path: str, user_id: int):
    file_record = FileModel(
        filename=os.path.basename(output_path),  # type: ignore 
        filepath=output_path, # type: ignore
        filesize=os.path.getsize(output_path), # type: ignore
        user_id=user_id # type: ignore
    )

    db.session.add(file_record)
    db.session.commit()

    return file_record

def save_converted_file(file, user_id=0) -> FileModel:

    original_name = os.path.splitext(file.filename)[0]
    original_ext = os.path.splitext(file.filename)[1].lower()

    output_path = get_output_path(original_name)

    temp_path = save_temp_file(file)
    
    if original_ext == '.txt':
        text_to_pdf(temp_path, output_path)
    elif original_ext == '.docx' or original_ext == '.doc':
        doc_to_pdf(temp_path, output_path)
    else:
        raise ValueError('Tipo de arquivo não suportado para conversão')
    
    file_record = save_file_in_database(output_path, user_id)

    return file_record
