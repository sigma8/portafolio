from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length



class ContactForm(FlaskForm):
    name = StringField("Name*", validators=[DataRequired()])
    subject = StringField("Subject*", validators=[DataRequired()])
    email = StringField("Email*", validators=[DataRequired(), Email(message="Enter a valid Email"), Length(max=120)])
    message = TextAreaField("Message*", validators=[DataRequired()])
    submit = SubmitField("Submit")
