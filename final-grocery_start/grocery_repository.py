from grocery_item import GroceryItem

#intermedio con la DB
class GroceryRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def get_all_items(self):
        return self.db_manager.get_all_items()

    def add_item(self, sku, name, description, price, quantity, expiration_date):
        self.db_manager.add_item(sku, name, description, price, quantity, expiration_date)

    def delete_item(self, sku):
        self.db_manager.delete_item(sku)

    def get_item_by_sku(self, sku):
        return self.db_manager.get_item_by_sku(sku)

    def update_item(self, sku, name, description, price, quantity, expiration_date):
        self.db_manager.update_item(sku, name, description, price, quantity, expiration_date)
