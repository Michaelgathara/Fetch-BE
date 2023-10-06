from flask import request, jsonify, make_response
from app.models import transactions, payer_balances

# Using the Blueprint from __init__.py
from . import routes_bp


@routes_bp.route('/add', methods=['POST'])
def add_points():
    """
    Adds points to a payer's balance and records the transaction.

    Expects a JSON payload with the following fields:
    - payer: A string representing the payer's name.
    - points: An integer representing the number of points to add or subtract.
    - timestamp: A string representing the timestamp of the transaction.

    Returns a JSON response with the updated payer balances.

    Raises:
    - 400 Bad Request: If the JSON payload is missing any of the required fields or if the fields have invalid types.
    """
    data = request.get_json()
    
    payer = data.get('payer')
    points = data.get('points')
    timestamp = data.get('timestamp')
    
    if points is None or not isinstance(points, int):
        return make_response('Invalid points', 400)
    if not payer or not isinstance(payer, str):
        return make_response('Invalid payer', 400)
    if not points or not isinstance(points, int):
        return make_response('Invalid points', 400)
    if not timestamp or not isinstance(timestamp, str):
        return make_response('Invalid timestamp', 400)
    
    transactions.append({
        'payer': payer,
        'points': points,
        'timestamp': timestamp
    })
    
    if payer in payer_balances:
        new_balance = payer_balances[payer] + points
        if new_balance < 0:
            return make_response('Insufficient points for payer', 400)
        payer_balances[payer] = new_balance
    else:
        if points < 0:
            return make_response('Insufficient points for payer', 400)
        payer_balances[payer] = points

    return make_response(jsonify(payer_balances), 200)
