from sqlalchemy import Column, Integer, ForeignKey, Enum
from sqlalchemy.orm import relationship
# from sqlalchemy.sql import func
from backend.app.database import Base
from backend.app.enums.CookingSkill import CookingSkill
from backend.app.enums.CuisineType import CuisineType
from backend.app.enums.DietaryRrestrictions import DietaryRestrictions


class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True)
    household_size = Column(Integer, nullable=False)
    dietary_restrictions = Column(Enum(DietaryRestrictions), default=DietaryRestrictions.NONE)
    cuisine_preference = Column(Enum(CuisineType), default=CuisineType.BANGLADESHI)
    cooking_skill = Column(Enum(CookingSkill), default=CookingSkill.INTERMEDIATE)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True) # one to one

    user = relationship("User", back_populates="profile") # one to one