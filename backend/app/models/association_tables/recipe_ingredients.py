from sqlalchemy import Column, Integer, Boolean, ForeignKey, String, Text, Table
from backend.app.database import Base

recipe_ingredients = Table(
    "recipe_ingredients",
    Base.metadata,
    Column("recipe_id", Integer, ForeignKey("recipes.id")),
    Column("ingredient_id", Integer, ForeignKey("ingredients.id")),
    Column("quantity", String(50)),
    Column("unit", String(50))
)