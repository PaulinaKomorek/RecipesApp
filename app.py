from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from database import *
from queries import *
import string
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://recipesapp:1234@localhost/recipesdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.route("/", methods=["get"])
def index():
    return render_template("index.html")


@app.route("/search", methods=["get"])
def search():
    products_idx = list(
        map(lambda i: int(i), request.args.get("products").split(",")))
    queries = get_recipies_by_products_idx(products_idx)
    return render_template("search.html", queries=queries)


@app.route("/recipe/<idx>", methods=["get"])
def recipe(idx: int):
    recipe = Recipe.query.get(idx)
    if recipe is None:
        return render_template("not_found.html")
    return render_template("recipe.html", recipe=recipe)


def random_string(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


@app.route("/form", methods=["get"])
def form():
    return render_template("form.html")


@app.route("/send_form", methods=["post"])
def send_form():
    title = request.form["title"]
    ingredients = request.form["ingredients"]
    recipe = request.form["recipe"]
    time = request.form["time"]
    difficulty = request.form["difficulty"]
    with open("sent_recipes/"+random_string()+".txt", "w") as fs:
        fs.write("\n\n".join([title, ingredients, recipe, time, difficulty]))
    return render_template("form_confirmation.html")
