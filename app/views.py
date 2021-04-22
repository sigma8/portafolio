from app import app
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class ContactForm(FlaskForm):
    name = StringField("Nombre", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    mensaje = StringField("Mensaje", validators=[DataRequired()])
    submit = SubmitField("Submit")

@app.route('/')
def index():
    return render_template("/index.html")

#localhost:500/user/name
@app.route('/user/<name>')
def user(name):
    return render_template("user.html", name=name)

#contact page

@app.route('/cv')
def cv():
    return render_template("cv.html")
#Pagina error personalizada error 404 y 500
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    name = None
    email = None
    mensaje = None
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        mensaje = form.mensaje.data
        form.name.data = ''
        form.email.data = ''
        form.mensaje.data = ''

    return render_template("contact.html", name=name, email=email, mensaje=mensaje, form=form)
