from sqlalchemy import Column, Enum, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship

# from sqlalchemy.sql import func
from backend.app.database import Base
from backend.app.enums.MealType import MealType
from backend.app.models.association_tables.meal_plan_recipes import meal_plan_recipes


class MealPlan(Base):
    __tablename__ = "meal_plans"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    meal_type = Column(Enum(MealType))
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="meal_plans") # one to many
    recipes = relationship("Recipe", secondary=meal_plan_recipes, back_populates="meal_plans") # many to many
    shopping_list = relationship("ShoppingList", back_populates="meal_plan", uselist=False) # one to one