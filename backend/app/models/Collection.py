from sqlalchemy import Column, Integer, ForeignKey, String, Text
from sqlalchemy.orm import relationship

# from sqlalchemy.sql import func
from backend.app.database import Base
from backend.app.models.association_tables.collection_recipes import collection_recipes


class Collection(Base):
    __tablename__ = "collections"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    description = Column(Text)
    user_id = Column(Integer, ForeignKey("users.id"))

    recipes = relationship("Recipe", secondary=collection_recipes, back_populates="collections") # many to many
    user = relationship("User", back_populates="collections") # one to many