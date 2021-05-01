from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length



class ContactForm(FlaskForm):
    name = StringField("Name:", validators=[DataRequired()])
    subject = StringField("Subject:", validators=[DataRequired()])
    email = StringField("Email:", validators=[DataRequired(), Email(), Length(max=120)])
    message = StringField("Message:", validators=[DataRequired()])
    submit = SubmitField("Submit")
