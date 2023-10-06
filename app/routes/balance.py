from flask import jsonify, make_response
from app.models import payer_balances

from . import routes_bp

@routes_bp.route('/balance', methods=['GET'])
def get_balance():
    """

    """
    return make_response(jsonify(payer_balances), 200)
