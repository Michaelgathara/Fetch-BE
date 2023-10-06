import json
from app import create_app, transactions, payer_balances
from app.utils import spend

app = create_app()

def test_spend():
    """
    TODO: 
    """
    
    client = app.test_client()
    
    # Prepare the initial transactions and payer balances
    print(f"Transactions before: {transactions}")
    transactions.extend([
        {'payer': 'DANNON', 'points': 1000, 'timestamp': '2022-01-01T12:00:00Z'},
        {'payer': 'UNILEVER', 'points': 2000, 'timestamp': '2022-01-01T13:00:00Z'}
    ])
    print(f"Transactions after: {transactions}")

    payer_balances.update({'DANNON': 1100, 'UNILEVER': 200, 'MILLER COORS': 10000})
    
    test_data = {
        'points': 5000
    }
    
    response = client.post('/spend',
                           data=json.dumps(test_data),
                           content_type='application/json')
    
    # Validate the response
    assert json.loads(response.data) == [
        {'payer': 'DANNON', 'points': 1000},
        {'payer': 'UNILEVER', 'points': 0},
        {'payer': 'MILLER COORS', 'points': 5300}
    ]
    
    # Validate payer balances
    assert payer_balances['DANNON'] == 1000
    assert payer_balances['UNILEVER'] == 0
    assert payer_balances['MILLER COORS'] == 5300

