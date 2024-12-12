
""" hola """
from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
import os
from dotenv import load_dotenv


load_dotenv()

mongo = PyMongo()
bcrypt = Bcrypt()
jwt = JWTManager()


def create_app():
    """Crea y configura la aplicacion Flask"""
    app = Flask(__name__)

    app.config["MONGO_URI"] = os.getenv("DATABASE_URL")
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET")


    mongo.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    CORS(app)

    return app