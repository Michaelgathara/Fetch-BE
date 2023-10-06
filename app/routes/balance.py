from flask import jsonify, make_response
from app.models import payer_balances

from . import routes_bp

@routes_bp.route('/balance', methods=['GET'])
def get_balance():
    """
    Returns the current balances for all payers.

    Returns a JSON response with the current payer balances.

    Raises:
    - None
    """
    return make_response(jsonify(payer_balances), 200)
