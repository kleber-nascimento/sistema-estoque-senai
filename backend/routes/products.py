from flask import Blueprint, request, jsonify
from models import Product
from db import db

# Criação do Blueprint para organizar as rotas de produtos
products_bp = Blueprint('products', __name__)

@products_bp.route('/products', methods=['POST'])
def create_product():
    """
    Rota para criar um novo produto.
    Aceita apenas requisições POST.
    """
    print("Requisição recebida no backend!")
    data = request.get_json()
    print(f"Dados recebidos: {data}")

    # Validação dos dados recebidos
    if not data or 'name' not in data or 'price' not in data or 'quantity' not in data:
        return jsonify({"message": "Dados inválidos!"}), 400

    # Capturando os dados
    name = data['name']
    description = data.get('description', '')  # Descrição é opcional
    price = data['price']
    quantity = data['quantity']

    # Criando o produto no banco de dados
    new_product = Product(name=name, description=description, price=price, quantity=quantity)
    db.session.add(new_product)
    db.session.commit()

    return jsonify({"message": "Produto cadastrado com sucesso!"}), 201

@products_bp.route('/products', methods=['GET'])
def get_products():
    """
    Rota para listar todos os produtos.
    Aceita apenas requisições GET.
    """
    products = Product.query.all()
    products_list = [
        {
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "price": product.price,
            "quantity": product.quantity,
        }
        for product in products
    ]
    return jsonify(products_list), 200
