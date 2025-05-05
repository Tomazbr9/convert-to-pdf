from flask import render_template, request
from flask import send_from_directory, current_app

from flask_login import current_user

from app.models.file import FileModel

from app.home.forms import FileForm
from app.home import home_bp

from app.services.file_service import save_converted_file

import os

@home_bp.route('/home', methods=['GET', 'POST'])
def home():
    file_record = None

    form = FileForm()
    if request.method == 'POST':

        if form.validate_on_submit():
            file = form.file.data

            try:
                # chama serviço para salvar o arquivo convertido e registra no banco
                file_record = save_converted_file(file)
            except ValueError as e:
                return f'Arquivo invalido para conversão: {e}'
    
    return render_template('home.html', form=form, file_record=file_record)
            
@home_bp.route('/media/<path:filename>')
def download_file(filename):
    media_path = os.path.join(current_app.root_path, 'media')
    # serve arquivo como download, buscando da pasta 'media'
    return send_from_directory(media_path, filename, as_attachment=True)

@home_bp.route('/my_pdfs')
def my_pdfs():
    # recupera todos os PDFs pertencentes ao usuário logado
    file_records = FileModel.query.filter_by(user_id=current_user.id).all()
    return render_template('user_pdfs.html', file_records=file_records)
