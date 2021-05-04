from flask import Flask
from flask_wtf import CsrfProtect

app = Flask(__name__, instance_relative_config=True)

app.config.from_object('config.DevelopmentConfig')
app.config.from_pyfile('config.py')

csrf = CsrfProtect(app) # Creando una instancia para CSRF para mi formulario
from app import views
