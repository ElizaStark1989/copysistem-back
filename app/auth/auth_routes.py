from flask import Blueprint, request, jsonify
from app import mongo, bcrypt


auth_routes = Blueprint("register", __name__)

@auth_routes.route("/", methods=["POST"])
def register():
    """maneja el registro de usuarios"""

    data = request.get_json()

    if not data.get("name") or not data.get("email") or not data.get("password"):
        return jsonify({"error": "Todos los campos son obligatorios"}), 400

    user= mongo.db.users.find_one({"email": data["email"]})
    if user:
        return jsonify({"error": "el usuario ya esta registrado"}), 400


    hashed_password = bcrypt.generate_password_hash(data["password"]).decode("utf-8")

    new_user = {
        "name": data["name"],
        "telefono": data["telefono"],
        "email": data["email"],
        "password": hashed_password,
        "role": "customer"
    }

    mongo.db.users.insert_one(new_user)

    return jsonify({"mensaje": "Usuario registrado con exito"}), 201