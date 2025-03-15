from sqlalchemy import Column, Table, Integer, String, ForeignKey, DateTime, func

from backend.app.database import Base

meal_plan_recipes = Table(
    "meal_plan_recipes",
    Base.metadata,
    Column("meal_plan_id", Integer, ForeignKey("recipes.id")),
    Column("recipe_id", Integer, ForeignKey("meal_plans.id")),
)