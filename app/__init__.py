from flask import Flask


app = Flask(__name__)

app.config['SECRET_KEY'] = "no es la contraseña final"

from app import views
