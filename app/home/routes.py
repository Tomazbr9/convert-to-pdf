from flask import render_template, request
from flask import send_from_directory, current_app

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
                file_record = save_converted_file(file)
            except ValueError:
                return 'Arquivo invalido para conversão'
    
    return render_template('home.html', form=form, file_record=file_record)
            
@home_bp.route('/media/<path:filename>')
def download_file(filename):
    media_path = os.path.join(current_app.root_path, 'media')
    return send_from_directory(media_path, filename, as_attachment=True)