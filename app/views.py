from app import app
from flask import render_template
import forms


#creando una ruta hacia index.html
@app.route('/')
def index():
    return render_template("/index.html")

#creando una ruta hacia about.html
@app.route('/about')
def about():
    return render_template("about.html")

#creando una ruta hacia resume.html

@app.route('/resume')
def resume():
    return render_template("resume.html")


#Pagina error personalizada error 404 y 500
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500

@app.route('/blog')
def blog():
    return render_template("blog.html")


#creando una ruta hacia contact.html
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    name = None
    subject = None
    email = None
    message = None
    form = forms.ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        subject =form.subject.data
        email = form.email.data
        message = form.message.data
        form.name.data = ''
        form.subject.data = ''
        form.email.data = ''
        form.message.data = ''

    return render_template("contact.html", name=name, subject=subject, email=email, message=message, form=form)
