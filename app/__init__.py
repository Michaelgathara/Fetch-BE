from flask import Flask
from .routes import routes_bp
from .models import transactions, payer_balances

def create_app():
    """
    TODO: 
    """
    app = Flask(__name__)
    
    app.register_blueprint(routes_bp)
    
    return app
