from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from database import *
import requests

 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://recipesapp:1234@localhost/recipesdb'
db.init_app(app)



@app.route("/", methods=["get"])
def index():
    return render_template("index.html")

@app.route("/search", methods=["get"])
def search():
    products=request.args.get("products").split(" ")
    return render_template("search.html")

@app.route("/recipe/<idx>", methods=["get"])
def recipe(idx: int):
    recipe=Recipe.query.get(idx)
    if recipe is None:
        return render_template("not_found.html")
    return render_template("recipe.html", recipe=recipe)