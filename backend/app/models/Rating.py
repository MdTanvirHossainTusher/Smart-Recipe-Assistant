from sqlalchemy import Column, Integer, Boolean, ForeignKey, String, Text
from sqlalchemy.orm import relationship

from backend.app.database import Base

class Rating(Base):
    __tablename__ = "ratings"

    id = Column(Integer, primary_key=True)
    score = Column(String(50))
    comment = Column(Text)
    recipe_id = Column(Integer, ForeignKey("recipes.id"))

    recipe = relationship("Recipe", back_populates="ratings") # one to many
