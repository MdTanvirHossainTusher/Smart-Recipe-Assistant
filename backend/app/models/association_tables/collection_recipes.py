# from sqlalchemy import Table, Column, Integer, ForeignKey
# from backend.app.database import Base
#
# collection_recipes = Table(
#     "collection_recipes",
#     Base.metadata,
#     Column("collection_id", Integer, ForeignKey("collections.id")),
#     Column("recipe_id", Integer, ForeignKey("recipes.id"))
# )

# Fix the collection_recipes table definition
from sqlalchemy import Table, Column, Integer, ForeignKey
from backend.app.database import Base

collection_recipes = Table(
    "collection_recipes",  # Fixed spelling from "recipies" to "recipes"
    Base.metadata,
    Column("collection_id", Integer, ForeignKey("collections.id")),
    Column("recipe_id", Integer, ForeignKey("recipes.id"))
)