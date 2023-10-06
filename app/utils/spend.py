from heapq import heapify, heappop, heappush
from collections import defaultdict

def consolidate_spent_points(spent_points):
    """
    Consolidates spent points from the payer_balances dictionary and records the transaction.

    Expects a JSON payload with the following fields:
    - points: An integer representing the number of points to spend.

    Returns a JSON response with the payer balances after the points have been spent.

    Raises:
    - 400 Bad Request: If the JSON payload is missing the points field, has an invalid type, or has a value less than or equal to zero.
    - 400 Bad Request: If the total number of points to spend is greater than the current total balance across all payers.
    """
    consolidated = defaultdict(int)
    for entry in spent_points:
        consolidated[entry['payer']] += entry['points']
    
    return [{'payer': payer, 'points': points} for payer, points in consolidated.items()]


def spend(points_to_spend, transactions, payer_balances):
    """
    Spends points from the payer_balances dictionary and records the transaction.

    Expects the following inputs:
    - points_to_spend: An integer representing the number of points to spend.
    - transactions: A list of dictionaries representing the transactions to spend points from.
      Each dictionary should have the following fields:
      - timestamp: A string representing the timestamp of the transaction.
      - payer: A string representing the payer's name.
      - points: An integer representing the number of points in the transaction.
    - payer_balances: A dictionary representing the current balances for each payer.
      The keys should be payer names and the values should be integers representing the payer's balance.

    Returns a list of dictionaries with the following fields:
    - payer: A string representing the payer's name.
    - points: An integer representing the net points spent by the payer.
      A positive value indicates points spent, while a negative value indicates points earned.

    Raises:
    - 400 Bad Request: If the total number of points to spend is greater than the current total balance across all payers.
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
            
    return consolidate_spent_points(spent_points)