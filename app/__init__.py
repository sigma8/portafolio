from flask import Flask
from flask_wtf import CsrfProtect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config.DevelopmentConfig')
app.config.from_pyfile('config.py')

db = SQLAlchemy(app) # Inicializando el Database handler SQLAlchemy


#csrf = CsrfProtect(app) # Creando una instancia para CSRF para mi formulario

from app import views
