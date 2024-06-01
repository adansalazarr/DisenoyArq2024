import sqlalchemy
from grocery_item import GroceryItem
from database_manager import DatabaseManager
from load_csv_to_db import load_csv_to_db

def create_database(database_uri):
    engine = sqlalchemy.create_engine(database_uri)
    GroceryItem.metadata.drop_all(engine)  # borra todas las tablas existentes
    GroceryItem.metadata.create_all(engine)  # Crea nuevas tablas

if __name__ == '__main__':
    DATABASE_URI = 'postgresql://sebas:newpass@localhost:5432/grocery_db'
    CSV_FILE_PATH = 'sample_grocery.csv'

    # Crear base de datos y tablas
    create_database(DATABASE_URI)

    # Cargar datos del CSV a la base de datos
    db_manager = DatabaseManager(DATABASE_URI)
    load_csv_to_db(CSV_FILE_PATH, db_manager)
