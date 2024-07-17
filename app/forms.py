from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired

class UploadForm(FlaskForm):
    pdf_file = FileField('PDF File', validators=[
        FileRequired(),
        FileAllowed(['pdf'], 'PDFs only!')
    ])
    additional_text = TextAreaField('Additional Text', validators=[DataRequired()])
    submit = SubmitField('Submit')