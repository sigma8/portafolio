from flask import Flask
from flask_wtf import CsrfProtect

app = Flask(__name__)

app.config['SECRET_KEY'] = "no es la contraseña final"
csrf = CsrfProtect(app)
from app import views
