import os
from flask import render_template, flash, redirect, url_for, request, current_app
from werkzeug.utils import secure_filename
from .forms import UploadForm
#import requests
from python_code.main import process_input


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']

@current_app.route('/', methods=['GET', 'POST'])
def upload_file():
    form = UploadForm()
    if form.validate_on_submit():
        file = form.pdf_file.data
        text = form.additional_text.data
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            # Process the file and text
            result = process_input(file_path, text)

            if result:
                return render_template('result.html', result=result)
            else:
                flash('Failed to process the file and text', 'danger')

    return render_template('upload.html', form=form)

