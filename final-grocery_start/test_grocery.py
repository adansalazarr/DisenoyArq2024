import pytest
from main import app
from grocery_repository import GroceryRepository
from flask import json

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            pass
        yield client

#Valida html GET
def test_get_items(client):
    prueba = client.get('/')
    assert prueba.status_code == 200
    assert b'Grocery Items' in prueba.data

#Valida lista datos GET
def test_get_items(client):
    prueba = client.get('/item')
    data = json.loads(prueba.data)
    assert isinstance(data, list)

#Prueba agregar item POST
def test_add_item(client):
    prueba = client.post('/item', data={
        'sku': 'Z999',
        'name': 'Prueba',
        'description': 'Prueba desc',
        'price': 10.99,
        'quantity': 5,
        'expiration_date': '2024-05-31'
    })
    assert prueba.status_code == 302

    #Prueba editar item POST
def test_edit_item(client):
    prueba = client.post('/item/Z999/', data={
        'name': 'asdfgh',
        'description': 'desc',
        'price': 15.0,
        'quantity': 10,
        'expiration_date': '2024-06-01'
    })
    assert prueba.status_code == 302

#Valida Eliminar item POST
def test_delete_item(client):
    prueba = client.delete('/item/Z999', data={
    })
    assert prueba.status_code == 302


