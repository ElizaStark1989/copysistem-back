from flask import Blueprint, jsonify, request
from app import mongo
from bson.objectid import ObjectId

user_routes = Blueprint("users", __name__)

@user_routes.route("/users", methods=["POST"])
def create_user():

    data = request.get_json()

    if not data.get("name") or not data.get("email"):
        return jsonify({"error": "El nombre y el correo son obligatorios"}), 400


    existing_user = mongo.db.users.find_one({"email": data["email"]})
    if existing_user:
        return jsonify({"error": "El usuario ya existe"}), 400


    user = {
        "name": data["name"],
        "email": data["email"]
    }

    result = mongo.db.users.insert_one(user)
    return jsonify({"mensaje": "Usuario creado", "user_id": str(result.inserted_id)}), 201

#leer todos los usuarios
@user_routes.route("/users", methods=["GET"])
def get_users():
    users = mongo.db.users.find()
    users_list = [
        {"id": str(user["_id"]), "name": user["name"], "email": user['email']}
        for user in users
    ]
    return jsonify({"users": users_list}), 200

#leer usuario por id
@user_routes.route("/users/<user_id>", methods=["GET"])
def get_user(user_id):
    from bson.errors import InvalidId

    try:
        user_id = user_id.strip()
        user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
        if not user:
            return jsonify({"error": "Usuario no encontrado"}), 404

        user_data = {"id": str(user["_id"]), "name": user["name"], "email": user["email"]}
        return jsonify({"user": user_data}), 200
    except InvalidId:
        return jsonify({"error": "ID invalido, no es un ObjectID valido"}), 400
    except Exception as e:
        return jsonify({"error": f"Error inesperado: {str(e)}"}), 500



#actualizar usuarios
@user_routes.route("/users/<user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()
    if not data.get("name") and not data.get("email"):
        return jsonify({"error": "Se requiere al menos un campo para actualizar"}), 400

    updated_data = {}
    if data.get("name"):
        updated_data["name"] = data["name"]
    if data.get("email"):
        updated_data["email"] = data["email"]

    try:
        result = mongo.db.users.update_one({"_id": ObjectId(user_id)}, {"$set": updated_data})
        if result.matched_count == 0:
            return jsonify({"error": "Usuario no encontrado"}), 404

        return jsonify({"mensaje": "Usuario actualizado"}), 200
    except Exception:
        return jsonify({"error": "ID invalido"}), 400

#eliminar usuario
@user_routes.route("/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    try:
        user_id = user_id.strip()
        result = mongo.db.users.delete_one({"_id": ObjectId(user_id)})
        if result.deleted_count == 0:
            return jsonify({"error": "Usuario no encontrado"}), 404
        return jsonify({"mensaje": "Usuario eliminado"}), 200
    except Exception:
        return jsonify({"error": "ID invalido"}), 400
    except Exception as e:
        return jsonify({"error": f"Error inesperado: {str(e)}"}), 500




