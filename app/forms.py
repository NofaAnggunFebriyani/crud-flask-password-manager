from app.models import Tambah
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired 

class addPlatform(FlaskForm):
    Platform = StringField(label='Platform', validators=[DataRequired()])

    Email = StringField(label='Email', validators=[DataRequired()])

    Password = StringField(label='Password', validators=[DataRequired()])

    Submit = SubmitField(label='Add Platform')




























