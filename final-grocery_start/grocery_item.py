from sqlalchemy import Column, String, Integer, Float, Date
from sqlalchemy.orm import declarative_base

Base = declarative_base()

#estrucutra de un ITEM
class GroceryItem(Base):
    __tablename__ = 'grocery_items'

    sku = Column(String, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    quantity = Column(Integer)
    expiration_date = Column(Date)