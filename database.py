from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Recipe(db.Model):
    __tablename__="recipes"
    idx=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(64))
    content=db.Column(db.String)
    time=db.Column(db.Integer)

    ingredients=db.relationship("Ingredient", backref="recipe", lazy=True)

class Product(db.Model):
    __tablename__="products"
    idx=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(64))
    category_idx=db.Column(db.Integer, db.ForeignKey("categories.idx"))

    ingredients=db.relationship("Ingredient", backref="product", lazy=True)

class Ingredient(db.Model):
    __tablename__="ingredients"
    recipe_idx=db.Column(db.Integer, db.ForeignKey("recipes.idx"), primary_key=True)
    product_idx=db.Column(db.Integer, db.ForeignKey("products.idx"), primary_key=True)
    amount=db.Column(db.String(64))

class Category(db.Model):
    __tablename__="categories"
    idx=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(64))
   
    products=db.relationship("Product", backref="category", lazy=True)
