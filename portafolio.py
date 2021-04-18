from flask import Flask, render_template
from random import choice
#crear una instancia Flask

app = Flask(__name__)


#crear una ruta (route decorator)
#index page
@app.route('/')
def index():
    return render_template("index.html")

#localhost:500/user/name
@app.route('/user/<name>')
def user(name):
    return render_template("user.html", name=name)

#contact page
@app.route('/contact')
def contact():
    return render_template("contact.html")

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
