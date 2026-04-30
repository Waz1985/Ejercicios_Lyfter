from flask import Flask, jsonify

from .config import Config
from .extensions import cache, db, jwt


def create_app(config_object=Config):
    app = Flask(__name__)
    app.config.from_object(config_object)

    db.init_app(app)
    jwt.init_app(app)
    cache.init_app(app)

    from .routes.auth import auth_bp
    from .routes.carts import carts_bp
    from .routes.invoices import invoices_bp
    from .routes.products import products_bp
    from .routes.users import users_bp

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(users_bp, url_prefix="/users")
    app.register_blueprint(products_bp, url_prefix="/products")
    app.register_blueprint(carts_bp, url_prefix="/carts")
    app.register_blueprint(invoices_bp, url_prefix="/invoices")

    @app.get("/health")
    def health():
        return jsonify({"status": "ok"})

    @app.cli.command("init-db")
    def init_db():
        from . import models  # noqa: F401

        db.create_all()
        print("Database initialized")

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"error": "Resource not found"}), 404

    return app
