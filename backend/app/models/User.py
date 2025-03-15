from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func, Boolean
from sqlalchemy.orm import relationship

# from sqlalchemy.sql import func
from backend.app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(120), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    deleted = Column(Boolean, default=False)
    # profile_id = Column(Integer, ForeignKey("profiles.id"))

    profile = relationship("Profile", back_populates="user", uselist=False, cascade="all, delete-orphan") # one to one

    # collections = relationship("Collection", back_populates="user") # one to many
    # meal_plans = relationship("MealPlan", back_populates="user") # one to many
