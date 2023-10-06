import json
from app import create_app, transactions, payer_balances

app = create_app()

def test_add():
    """
    TODO: 
    """
    client = app.test_client()
    
    transactions.clear()
    payer_balances.clear()
    
    
    test_data_and_expected_balances = [
        ({'payer': 'DANNON', 'points': 300, 'timestamp': '2022-10-31T10:00:00Z'}, 
         {'DANNON': 300}),
        ({'payer': 'UNILEVER', 'points': 200, 'timestamp': '2022-10-31T11:00:00Z'}, 
         {'DANNON': 300, 'UNILEVER': 200}),
        ({'payer': 'DANNON', 'points': -200, 'timestamp': '2022-10-31T15:00:00Z'}, 
         {'DANNON': 100, 'UNILEVER': 200}),
        ({'payer': 'MILLER COORS', 'points': 10000, 'timestamp': '2022-11-01T14:00:00Z'},
         {'DANNON': 100, 'UNILEVER': 200, 'MILLER COORS': 10000}),
        ({'payer': 'DANNON', 'points': 1000, 'timestamp': '2022-11-02T14:00:00Z'}, 
         {'DANNON': 1100, 'UNILEVER': 200, 'MILLER COORS': 10000})
    ]
    
    for test_data, expected_balance in test_data_and_expected_balances:
        response = client.post('/add',
                               data=json.dumps(test_data),
                               content_type='application/json')
        
        print(f"Actual: {payer_balances}\nExpected: {expected_balance}")
        assert payer_balances == expected_balance

