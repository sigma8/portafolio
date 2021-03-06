from app import app, db
from flask import render_template, send_file, send_from_directory, safe_join, abort
from .forms import ContactForm
from .models import Contact



#creando una ruta hacia index.html
@app.route('/')
def index():
    print(app.config)
    return render_template("/index.html")

#creando una ruta hacia about.html
@app.route('/about')
def about():
    return render_template("about.html")

#creando una ruta hacia resume.html

@app.route('/resume')
def resume():
    return render_template("resume.html")

@app.route("/get-pdf")
def get_pdf():
    filename = "cv_en_Jose_Tortolero.pdf"
    try:
        return send_from_directory(app.config['CLIENT_PDF'], filename=filename, as_attachment=True)
    except FileNotFoundError:
        abort(404)


#Pagina error personalizada error 404 y 500
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500

@app.route('/work')
def work():
    return render_template("work.html")


#creando una ruta hacia contact.html
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    name = None
    subject = None
    email = None
    message = None
    form = ContactForm()
    if form.validate_on_submit():
        #user = test.query.filter_by(email=form.email.data).first()
        contacto = Contact(name=form.name.data,
                        subject=form.subject.data,
                        email = form.email.data,
                        message = form.message.data)
        db.session.add(contacto)
        db.session.commit()
        form.name.data = ''
        form.subject.data = ''
        form.email.data = ''
        form.message.data = ''
    return render_template("contact.html", name=name, subject=subject, email=email, message=message, form=form)
