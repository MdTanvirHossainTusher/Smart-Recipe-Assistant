from sqlalchemy import Column, Integer, Float, Boolean, ForeignKey, String, Text
from sqlalchemy.orm import relationship

from backend.app.database import Base

class NutritionInfo(Base):
    __tablename__ = "nutrition_info"

    id = Column(Integer, primary_key=True)
    calories = Column(Float, nullable=True)
    protein = Column(Float, nullable=True)
    carbohydrates = Column(Float, nullable=True)
    fat = Column(Float, nullable=True)
    fiber = Column(Float, nullable=True)
    others = Column(Float, nullable=True)
    ingredients_id = Column(Integer, ForeignKey("ingredients.id"), unique=True) # One to One

    ingredients = relationship("Ingredient", back_populates="nutrition_info") # One to One