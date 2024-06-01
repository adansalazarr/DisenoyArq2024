import csv
from database_manager import DatabaseManager

def load_csv_to_db(file_path, db_manager):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            db_manager.add_item(
                sku=row['SKU'],
                name=row['Name'],
                description=row['Description'],
                price=float(row['Price']),
                quantity=int(row['Quantity']),
                expiration_date=row['Expiration Date']
            )
