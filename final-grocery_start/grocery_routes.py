from flask import Blueprint, request, render_template, redirect, url_for, jsonify
from grocery_repository import GroceryRepository
from currency_converter import CurrencyConverter

grocery_routes = Blueprint('grocery_routes', __name__)

#instancia de bd y currency
def init_repository(db_manager, api_key):
    global repository, converter
    repository = GroceryRepository(db_manager)
    converter = CurrencyConverter(api_key)

#definimos raiz para html y mostrar todos los items
@grocery_routes.route('/')
def index():
    items = repository.get_all_items()
    return render_template('index.html', items=items)

#request para ver todos los ITEMS
@grocery_routes.route('/item', methods=['GET'])
def get_all_items():
    items = repository.get_all_items()
    items_json = [
        {
            'sku': item.sku,
            'name': item.name,
            'description': item.description,
            'price': item.price,
            'quantity': item.quantity,
            'expiration_date': item.expiration_date
        } for item in items
    ]
    return jsonify(items_json)

#agregar ITEM
@grocery_routes.route('/item', methods=['POST'])
def add_item():
    sku = request.form['sku']
    name = request.form['name']
    description = request.form['description']
    price = float(request.form['price'])
    quantity = int(request.form['quantity'])
    expiration_date = request.form['expiration_date']
    repository.add_item(sku, name, description, price, quantity, expiration_date)
    return redirect(url_for('grocery_routes.index'))

#Elminar ITEM por SKU
@grocery_routes.route('/item/<sku>', methods=['DELETE'])
def delete_item(sku):
    repository.delete_item(sku)
    return redirect(url_for('grocery_routes.index'))

#Editar ITEM por SKU
@grocery_routes.route('/item/<sku>', methods=['GET', 'POST'])
def edit_item(sku):
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = float(request.form['price'])
        quantity = int(request.form['quantity'])
        expiration_date = request.form['expiration_date']
        repository.update_item(sku, name, description, price, quantity, expiration_date)
        return redirect(url_for('grocery_routes.index'))
    item = repository.get_item_by_sku(sku)
    return render_template('index.html', item_to_edit=item)

#Currency converter con API basado en SKU
@grocery_routes.route('/item/<sku>/convert', methods=['GET'])
def convert_price(sku):
    currency = request.args.get('currency')
    item = repository.get_item_by_sku(sku)
    
    try:
        converted_price = converter.convert_currency(item.price, 'USD', currency) 
        item_json = {
            'sku': item.sku,
            'name': item.name,
            'description': item.description,
            'price': converted_price,
            'quantity': item.quantity,
            'expiration_date': item.expiration_date,
            'currency': currency
        }
        return jsonify(item_json)
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
