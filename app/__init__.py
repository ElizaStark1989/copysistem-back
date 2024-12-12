
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

    from app.auth.auth_routes import auth_routes
    from app.auth.login_routes import login_routes
    from app.main.main_routes import main_routes
    from app.main.user_routes import user_routes

    app.register_blueprint(auth_routes, url_prefix="/auth")
    app.register_blueprint(login_routes, url_prefix="/login")
    app.register_blueprint(main_routes, url_prefix="/api")
    app.register_blueprint(user_routes, url_prefix="/api")

    return app