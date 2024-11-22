from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from models import User, db

users_bp = Blueprint("users", __name__)

@users_bp.route("/register", methods=["POST"])
def register_user():
    # Captura os dados enviados no corpo da requisição
    data = request.get_json()
    
    # Valida se os campos obrigatórios estão presentes
    if not all(key in data for key in ("name", "email", "password", "cpf", "phone")):
        return jsonify({"message": "Todos os campos são obrigatórios."}), 400

    name = data["name"]
    email = data["email"]
    password = data["password"]
    cpf = data["cpf"]
    phone = data["phone"]
    
    # Gera o hash da senha
    hashed_password = generate_password_hash(password, method="pbkdf2:sha256", salt_length=16)

    # Verifica se o email já está registrado
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({"message": "Email já registrado."}), 409
    
    # Cria um novo usuário
    new_user = User(name=name, email=email, password=hashed_password, cpf=cpf, phone=phone)
    
    # Adiciona o novo usuário ao banco de dados
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"message": "Usuário registrado com sucesso!"}), 201

from werkzeug.security import check_password_hash

@users_bp.route("/login", methods=["POST"])
def login_user():
    # Captura os dados enviados na requisição
    data = request.get_json()

    # Valida se os campos obrigatórios estão presentes
    if not all(key in data for key in ("email", "password")):
        return jsonify({"message": "Email e senha são obrigatórios."}), 400

    email = data["email"]
    password = data["password"]

    # Busca o usuário pelo email
    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({"message": "Usuário não encontrado."}), 404

    # Verifica se a senha está correta
    if not check_password_hash(user.password, password):
        return jsonify({"message": "Senha incorreta."}), 401

    return jsonify({"message": "Login bem-sucedido!"}), 200

