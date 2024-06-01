import sqlalchemy
from sqlalchemy.orm import sessionmaker
from grocery_item import GroceryItem

#manejador de DB
class DatabaseManager:
    #iniciamos DB
    def __init__(self, database_uri):
        self.engine = sqlalchemy.create_engine(database_uri)
        self.Session = sessionmaker(bind=self.engine)

    def get_all_items(self):
        session = self.Session()
        items = session.query(GroceryItem).all()
        session.close()
        return items

    def add_item(self, sku, name, description, price, quantity, expiration_date):
        session = self.Session()
        item = GroceryItem(sku=sku, name=name, description=description, price=price, quantity=quantity, expiration_date=expiration_date)
        session.add(item)
        session.commit()
        session.close()

    def delete_item(self, sku):
        session = self.Session()
        item = session.query(GroceryItem).filter_by(sku=sku).first()
        if item:
            session.delete(item)
            session.commit()
        session.close()

    def get_item_by_sku(self, sku):
        session = self.Session()
        item = session.query(GroceryItem).filter_by(sku=sku).first()
        session.close()
        return item

    def update_item(self, sku, name, description, price, quantity, expiration_date):
        session = self.Session()
        item = session.query(GroceryItem).filter_by(sku=sku).first()
        if item:
            item.name = name
            item.description = description
            item.price = price
            item.quantity = quantity
            item.expiration_date = expiration_date
            session.commit()
        session.close()
