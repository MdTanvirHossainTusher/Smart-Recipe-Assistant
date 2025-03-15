from sqlalchemy import Column, Integer, Boolean, ForeignKey, String, Text
from sqlalchemy.orm import relationship

from backend.app.database import Base
from backend.app.models.association_tables.recipe_ingredients import recipe_ingredients


class Ingredient(Base):
    __tablename__ = "ingredients"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    is_allergen = Column(Boolean, default=False)
    category_id = Column(Integer, ForeignKey("categories.id"))
    nutrition_info_id = Column(Integer, ForeignKey("nutrition_info.id"))

    # category = relationship("Category", back_populates="ingredients")

    nutrition_info = relationship("NutritionInfo", back_populates="ingredients") # one to one
    recipes = relationship("Recipe", secondary=recipe_ingredients, back_populates="ingredients") # many to many

    # shopping_list_items = relationship("ShoppingListItem", back_populates="ingredient") # one to many