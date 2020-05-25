from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from database import *
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://recipesapp:1234@localhost/recipesdb'
db.init_app(app)

@app.route('/')
def index():
    ingredients=Recipe.query.first()
    return ""