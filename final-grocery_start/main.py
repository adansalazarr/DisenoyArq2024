from flask import Flask
from grocery_routes import grocery_routes, init_repository
from database_manager import DatabaseManager

app = Flask(__name__)

# Crear instancia de DatabaseManager
database_uri = 'postgresql://sebas:newpass@localhost:5432/grocery_db'
db_manager = DatabaseManager(database_uri)
api_key = 'ef9232b5374573e70f230dac3f6478f1'

# Inicializar repository en grocery_routes
init_repository(db_manager, api_key)

app.register_blueprint(grocery_routes)

if __name__ == '__main__':
    app.run(debug=True)
