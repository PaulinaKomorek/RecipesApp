from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from database import *
from queries import *
import config_loader 

app = Flask(__name__)
app.config.from_object('config_loader')
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
