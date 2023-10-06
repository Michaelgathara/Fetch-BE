from flask import request, jsonify, make_response
from app.models import transactions, payer_balances
from app.utils import spend

# Using the Blueprint from __init__.py
from . import routes_bp

@routes_bp.route('/spend', methods=['POST'])
def spend_points():
    # Parse the JSON request body
    data = request.get_json()
    
    points_to_spend = data.get('points')
    
    # Validate the input
    if not points_to_spend or not isinstance(points_to_spend, int) or points_to_spend <= 0:
        return make_response('Invalid points', 400)
    
    # Check if user has enough points
    total_points = sum(payer_balances.values())
    if points_to_spend > total_points:
        return make_response('Not enough points', 400)
    
    # Apply the spending algorithm to determine which payer points to spend
    spent_points = spend(points_to_spend, transactions, payer_balances)
    
    # Update payer balances based on spent points
    for spent in spent_points:
        payer_name = spent['payer']
        points_spent = spent['points']
        
        # Subtract the spent points from the payer balances
        payer_balances[payer_name] += points_spent  # points_spent is negative
    

    return make_response(jsonify(spent_points), 200)
