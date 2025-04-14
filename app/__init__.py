from flask import Flask

# Factory function to create the Flask app
def create_app():
    app = Flask(__name__)

    # Import and register routes
    from .server import app as server_app
    app.register_blueprint(server_app)

    return app