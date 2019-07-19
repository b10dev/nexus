"""
Author: Jay
This is the python file that will:
    - Import Flask
    - Declare the instance of the app
    - Import the blueprints from the nexus folder
"""
from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

from nexus.home.routes import home
from nexus.login.routes import login

app.register_blueprint(home)
app.register_blueprint(login)
