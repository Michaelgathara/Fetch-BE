from flask import request, jsonify, make_response
from app.models import transactions, payer_balances
from app.utils import spend
from . import routes_bp

@routes_bp.route('/spend', methods=['POST'])
def spend_points():
    """
    TODO: 
    """
    data = request.get_json()
    
    points_to_spend = data.get('points')
    
    if not points_to_spend or not isinstance(points_to_spend, int) or points_to_spend <= 0:
        return make_response('Invalid points', 400)
    
    total_points = sum(payer_balances.values())
    if points_to_spend > total_points:
        return make_response('Not enough points', 400)
    
    spent_points = spend(points_to_spend, transactions, payer_balances)
    
    for spent in spent_points:
        payer_name = spent['payer']
        points_spent = spent['points']
        
        payer_balances[payer_name] += points_spent 
    

    return make_response(jsonify(spent_points), 200)
