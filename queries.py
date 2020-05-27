from database import *


def get_recipies_by_products_idx(products_idx: list):
	recipes = Recipe.query.filter(Recipe.ingredients.any(Ingredient.product_idx.in_(products_idx))).all()
	recipes.sort(key=lambda recipe: len(set(products_idx) & set(map(lambda ingredient: ingredient.product_idx, recipe.ingredients))), reverse=True)
	return recipes
