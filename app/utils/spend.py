from heapq import heapify, heappop, heappush

def spend(points_to_spend, transactions, payer_balances):
    """
    TODO: 
    """
    min_heap = [(trans['timestamp'], trans['payer'], trans['points']) for trans in transactions]
    heapify(min_heap)
    
    spent_points = []
    remaining_points = points_to_spend
    
    while remaining_points > 0:
        timestamp, payer, points = heappop(min_heap)
        
        spend_from_this_trans = min(points, remaining_points)
        
        remaining_points -= spend_from_this_trans
        
        points -= spend_from_this_trans
        if points > 0:
            heappush(min_heap, (timestamp, payer, points))
        
        payer_balances[payer] -= spend_from_this_trans
        
        if spent_points and spent_points[-1]['payer'] == payer:
            spent_points[-1]['points'] -= spend_from_this_trans 
        else:
            spent_points.append({'payer': payer, 'points': -spend_from_this_trans})
            
    return spent_points
