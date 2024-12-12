from flask import Blueprint, jsonify


main_routes = Blueprint("main", __name__)

@main_routes.route("/", methods=["GET"])
def home():
    """ruta principal de la API"""

    return jsonify({"message": "Bienvenidos al backend de Copysistem"})