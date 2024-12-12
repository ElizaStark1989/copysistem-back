from flask import Blueprint, jsonify



main_routes = Blueprint("main_routes", __name__)

@main_routes.route("/", methods=["GET"])
def home():

    return jsonify({"message": "Bienvenidos al backend de Copysistem"}), 400

@main_routes.route("/status", methods=["GET"])
def status():
    return jsonify({"status": "OK", "message": "El servidor esta funcionando correctamente"}), 200

