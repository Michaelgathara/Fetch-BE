from heapq import heapify, heappop, heappush

def spend(points_to_spend, transactions, payer_balances):
    # Create a min-heap based on the transaction timestamps
    min_heap = [(trans['timestamp'], trans['payer'], trans['points']) for trans in transactions]
    heapify(min_heap)
    
    spent_points = []
    remaining_points = points_to_spend
    
    while remaining_points > 0:
        timestamp, payer, points = heappop(min_heap)
        
        # Determine how many points to spend from this transaction
        spend_from_this_trans = min(points, remaining_points)
        
        # Update the remaining points to be spent
        remaining_points -= spend_from_this_trans
        
        # Update the points in this transaction
        points -= spend_from_this_trans
        if points > 0:
            heappush(min_heap, (timestamp, payer, points))
        
        # Update the payer balances
        payer_balances[payer] -= spend_from_this_trans
        
        # Update the spent points list
        if spent_points and spent_points[-1]['payer'] == payer:
            spent_points[-1]['points'] -= spend_from_this_trans  # Subtract as they are negative
        else:
            spent_points.append({'payer': payer, 'points': -spend_from_this_trans})  # Negative points spent
            
    return spent_points
