from sqlalchemy import Column, Enum, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship

# from sqlalchemy.sql import func
from backend.app.database import Base
from backend.app.enums.MealType import MealType
from backend.app.models.association_tables.meal_plan_recipes import meal_plan_recipes


class ShoppingList(Base):
    __tablename__ = "shopping_lists"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    meal_plan_id = Column(Integer, ForeignKey('meal_plans.id'), unique=True) # one to one

    meal_plan = relationship("MealPlan", back_populates="shopping_list") # one to one
    shopping_list_items = relationship("ShoppingListItem", back_populates="shopping_list") # one to many


