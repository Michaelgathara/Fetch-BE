from flask import request, jsonify, make_response
from app.models import transactions, payer_balances
from app.utils import spend
from . import routes_bp

@routes_bp.route('/spend', methods=['POST'])
def spend_points():
    """
    Spends points from the payer_balances dictionary and records the transaction.

    Expects a JSON payload with the following fields:
    - points: An integer representing the number of points to spend.

    Raises:
    - 400 Bad Request: If the JSON payload is missing the points field, has an invalid type, or has a value less than or equal to zero.
    - 400 Bad Request: If the total number of points to spend is greater than the current total balance across all payers.
    """
    data = request.get_json()
    
    points_to_spend = data.get('points')
    
    if not points_to_spend or not isinstance(points_to_spend, int) or points_to_spend <= 0:
        return make_response('Invalid points', 400)
    
    total_points = sum(payer_balances.values())
    if points_to_spend > total_points:
        return make_response('Not enough points', 400)
    
    spent_points = spend(points_to_spend, transactions, payer_balances)
    
    return make_response(jsonify(spent_points), 200)