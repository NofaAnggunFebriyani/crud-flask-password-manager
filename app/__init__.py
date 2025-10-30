from flask import Flask
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__) 
Scss(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mp.db'
app.config['SECRET_KEY'] = '669aafaa72fc94fe4626a5d4662639'
db = SQLAlchemy(app)


from app import views



