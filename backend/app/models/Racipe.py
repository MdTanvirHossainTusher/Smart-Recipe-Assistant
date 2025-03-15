# from sqlalchemy import Column, Integer, Enum, String, Text, Boolean
# from sqlalchemy.orm import relationship
#
# # from sqlalchemy.sql import func
# from backend.app.database import Base
# from backend.app.enums.CuisineType import CuisineType
# from backend.app.models.association_tables.collection_recipes import collection_recipes
# from backend.app.models.association_tables.meal_plan_recipes import meal_plan_recipes
# from backend.app.models.association_tables.recipe_ingredients import recipe_ingredients
#
#
# class Recipe(Base):
#     __tablename__ = "recipes"
#
#     id = Column(Integer, primary_key=True)
#     name = Column(String(50))
#     description = Column(Text)
#     instructions = Column(Text)
#     is_favorite = Column(Boolean, default=False)
#     cooking_time = Column(Integer, description="In Minutes")
#     average_rating = Column(Integer, default=0)
#     image_url = Column(String(1000))
#     cuisine_type = Column(Enum(CuisineType))
#
#     ratings = relationship("Rating", back_populates="recipe") # One-to-Many
#     ingredients = relationship("Ingredient", secondary=recipe_ingredients, back_populates="recipes") # Many-to-Many
#     collections = relationship("Collection", secondary=collection_recipes, back_populates="recipes") # Many-to-Many
#     meal_plans = relationship("MealPlan", secondary=meal_plan_recipes, back_populates="recipes") # Many-to-Many

# # Fix the Recipe class
# from sqlalchemy import Column, Integer, Enum, String, Text, Boolean
# from sqlalchemy.orm import relationship
# from backend.app.database import Base
# from backend.app.enums.CuisineType import CuisineType
# from backend.app.models.association_tables.collection_recipes import collection_recipes
# from backend.app.models.association_tables.meal_plan_recipes import meal_plan_recipes
# from backend.app.models.association_tables.recipe_ingredients import recipe_ingredients
#
# class Recipe(Base):
#     __tablename__ = "recipes"
#     id = Column(Integer, primary_key=True)
#     name = Column(String(50))
#     description = Column(Text)
#     instructions = Column(Text)
#     is_favorite = Column(Boolean, default=False)
#     cooking_time = Column(Integer, description="In Minutes")
#     average_rating = Column(Integer, default=0)
#     image_url = Column(String(1000))
#     cuisine_type = Column(Enum(CuisineType))
#     ratings = relationship("Rating", back_populates="recipe")  # One-to-Many
#     ingredients = relationship("Ingredient", secondary=recipe_ingredients, back_populates="recipes")  # Many-to-Many
#     collections = relationship("Collection", secondary=collection_recipes, back_populates="recipes")  # Many-to-Many
#     meal_plans = relationship("MealPlan", secondary=meal_plan_recipes, back_populates="recipes")  # Many-to-Many


# backend/app/models/Recipe.py
from sqlalchemy import Column, Integer, Enum, String, Text, Boolean
from sqlalchemy.orm import relationship
from backend.app.database import Base
from backend.app.enums.CuisineType import CuisineType

# Import association tables - but don't import the Recipe model from them
from backend.app.models.association_tables.collection_recipes import collection_recipes
from backend.app.models.association_tables.meal_plan_recipes import meal_plan_recipes
from backend.app.models.association_tables.recipe_ingredients import recipe_ingredients


class Recipe(Base):
    __tablename__ = "recipes"  # Make sure this is correct
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    description = Column(Text)
    instructions = Column(Text)
    is_favorite = Column(Boolean, default=False)
    cooking_time = Column(Integer, description="In Minutes")
    average_rating = Column(Integer, default=0)
    image_url = Column(String(1000))
    cuisine_type = Column(Enum(CuisineType))

    # Relationships
    ratings = relationship("Rating", back_populates="recipe")  # One-to-Many
    ingredients = relationship("Ingredient", secondary=recipe_ingredients, back_populates="recipes")  # Many-to-Many
    collections = relationship("Collection", secondary=collection_recipes, back_populates="recipes")  # Many-to-Many
    meal_plans = relationship("MealPlan", secondary=meal_plan_recipes, back_populates="recipes")  # Many-to-Many