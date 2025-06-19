from flask import Flask
from app.extensions import db, migrate, jwt, api
from app.config import Config
from app.routes import cliente_routes, auth_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app)
    jwt.init_app(app)
    api.init_app(app)

    api.add_namespace(cliente_routes.clientes_ns, path="/clientes")
    api.add_namespace(auth_routes.auth_ns, path="/auth")

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
