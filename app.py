from app import create_app
from app.main.main_routes import main_routes
from app.auth.auth_routes import auth_routes
from app.auth.login_routes import login_routes

app = create_app()

app.register_blueprint(main_routes, url_prefix= "/api")
app.register_blueprint(auth_routes, url_prefix="/api/register")
app.register_blueprint(login_routes, url_prefix="/api/login")

if __name__== "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)