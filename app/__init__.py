from flask import Flask
from .routes import routes_bp
from .models import transactions, payer_balances

def create_app():
    app = Flask(__name__)
    
    # Register the routes blueprint
    app.register_blueprint(routes_bp)
    
    return app
