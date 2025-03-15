from sqlalchemy import Column, Float, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

# from sqlalchemy.sql import func
from backend.app.database import Base


class ShoppingListItem(Base):
    __tablename__ = "shopping_list_items"

    id = Column(Integer, primary_key=True)
    quantity = Column(Float)
    unit = Column(String(50))
    ingredient_id = Column(Integer, ForeignKey('ingredients.id'))
    shopping_list_id = Column(Integer, ForeignKey('shopping_lists.id'))

    shopping_list = relationship("ShoppingList", back_populates="shopping_list_items") # one to many

    # ingredient = relationship("Ingredient", back_populates="shopping_list_items")