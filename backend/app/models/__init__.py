# from backend.app.models.Collection import Collection
# from backend.app.models.Ingredient import Ingredient
# from backend.app.models.MealPlan import MealPlan
# from backend.app.models.NutritionInfo import NutritionInfo
# from backend.app.models.Profile import Profile
# from backend.app.models.Rating import Rating
# from backend.app.models.ShoppingList import ShoppingList
# from backend.app.models.User import User
# # from backend.app.models.Recipe import Recipe
#
# # Import association tables
# from backend.app.models.association_tables.collection_recipes import collection_recipes
# from backend.app.models.association_tables.meal_plan_recipes import meal_plan_recipes
# from backend.app.models.association_tables.recipe_ingredients import recipe_ingredients

# backend/app/models/__init__.py
from backend.app.database import Base

# First, import association tables
# from backend.app.models.association_tables.collection_recipes import collection_recipes
# from backend.app.models.association_tables.meal_plan_recipes import meal_plan_recipes
# from backend.app.models.association_tables.recipe_ingredients import recipe_ingredients

# from backend.app.models.Recipe import Recipe
# from backend.app.models.Collection import Collection
# from backend.app.models.Ingredient import Ingredient
# from backend.app.models.MealPlan import MealPlan
# from backend.app.models.NutritionInfo import NutritionInfo
# from backend.app.models.Rating import Rating
# from backend.app.models.ShoppingList import ShoppingList
from backend.app.models.User import User
from backend.app.models.Profile import Profile
