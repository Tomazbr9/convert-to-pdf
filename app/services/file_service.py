from flask import current_app

from converters.pdf_from_text import text_to_pdf

from werkzeug.utils import secure_filename

from models.file import FileModel

import os

import tempfile

def save_converted_file(file, user_id=0):
    original_name = os.path.splitext(file.filename)[0]
    original_ext = os.path.splitext(file.filename)[1].lower()

    media_path = os.path.join(current_app.root_path, 'media')
    os.makedirs(media_path, exist_ok=True)
    output_path = os.path.join(media_path, f'{original_name}.pdf')

    temp_dir = tempfile.mkdtemp()
    temp_path = os.path.join(temp_dir, secure_filename(file.filename))
    file.save(temp_path)

    if original_ext == '.txt':
        text_to_pdf(temp_path, output_path)
    else:
        raise ValueError('Tipo de arquivo não suportado para conversão')
    
    file_record = FileModel(
        filename=file.filename,  # type: ignore 
        filepath=output_path, # type: ignore
        filesize=os.path.getsize(output_path), # type: ignore
        user_id=user_id # type: ignore
    )
    from app import db
    db.session.add(file_record)
    db.session.commit()

    return file_record


if __name__ == '__main__':
    x = save_converted_file('ola.txt')