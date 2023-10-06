from flask import request, jsonify, make_response
from app.models import transactions, payer_balances

# Using the Blueprint from __init__.py
from . import routes_bp


@routes_bp.route('/add', methods=['POST'])
def add_points():
    """
        
    """
    data = request.get_json()
    
    payer = data.get('payer')
    points = data.get('points')
    timestamp = data.get('timestamp')
    
    # validation
    if not payer or not isinstance(payer, str):
        return make_response('Invalid payer', 400)
    if not points or not isinstance(points, int) or points <= 0:
        return make_response('Invalid points', 400)
    if not timestamp or not isinstance(timestamp, str):
        return make_response('Invalid timestamp', 400)
    
    # Update the transactions
    transactions.append({
        'payer': payer,
        'points': points,
        'timestamp': timestamp
    })
    
    # Update the balances
    if payer in payer_balances:
        payer_balances[payer] += points
    else:
        payer_balances[payer] = points

    return make_response('', 200)
