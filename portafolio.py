from flask import Flask, render_template

#crear una instancia Flask

app = Flask(__name__)


#crear una ruta (route decorator)

@app.route('/')

def index():
    return render_template("index.html")

#localhost:500/user/name
@app.route('/user/<name>')

def user(name):
    return render_template("user.html", name=name)

@app.route('/contact')
def contact():
    return render_template("contact.html")



#Pagina error personalizada

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500
