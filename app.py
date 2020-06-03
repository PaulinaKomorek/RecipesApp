from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from database import db
from queries import *
from config import URI, TRACK

app = Flask(__name__)

if True:
	app.config['SQLALCHEMY_DATABASE_URI'] = URI
else:
	app.config['SQLALCHEMY_DATABASE_URI'] = ''
	
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.route("/", methods=["get"])
def index():
	return render_template("index.html")


@app.route("/search", methods=["get"])
def search():
	products_idx = list(map(lambda i: int(i), request.args.get("products").split(",")))
	queries = get_recipies_by_products_idx(products_idx)
	return render_template("search.html", queries=queries)


@app.route("/recipe/<idx>", methods=["get"])
def recipe(idx: int):
	return render_template("recipe.html")
