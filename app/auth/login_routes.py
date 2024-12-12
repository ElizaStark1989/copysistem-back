from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from datetime import timedelta
from app import mongo, bcrypt

login_routes = Blueprint("login", __name__)

@login_routes.route("/", methods=["POST"])
def login():
    """ Maneja el inicio de seccion de ususarios"""

    data = request.get_json()

    if not data.get("email") or not data.get("password"):
        return jsonify({"error": "Email y contraseña son obligatorios"}), 400

    user = mongo.db.users.find_one({"email": data["email"]})
    if not user:
        return jsonify({"error": "EL usuario no esta registrado"}), 404

    if not bcrypt.check_password_hash(user["password"], data["password"]):
        return jsonify({"error": "Contraseña incorrecta"}), 401

    token = create_access_token(identity=str(user["_id"]), expires_delta=timedelta(hours=1))
    return jsonify({"mensaje": "Login exitoso", "token": token}), 200
