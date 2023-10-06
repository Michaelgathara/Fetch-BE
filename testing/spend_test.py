import json
from app import create_app, transactions, payer_balances
from app.utils import spend

app = create_app()

def test_spend():
    # Create a test client
    client = app.test_client()
    
    # Prepare the initial transactions and payer balances
    transactions.extend([
        {'payer': 'DANNON', 'points': 1000, 'timestamp': '2022-01-01T12:00:00Z'},
        {'payer': 'UNILEVER', 'points': 2000, 'timestamp': '2022-01-01T13:00:00Z'}
    ])
    payer_balances.update({'DANNON': 1000, 'UNILEVER': 2000})
    
    # Prepare the test data
    test_data = {
        'points': 1500
    }
    
    # Send POST request to /spend endpoint
    response = client.post('/spend',
                           data=json.dumps(test_data),
                           content_type='application/json')
    
    # Validate the response
    assert response.status_code == 200
    assert json.loads(response.data) == [
        {'payer': 'DANNON', 'points': -1000},
        {'payer': 'UNILEVER', 'points': -500}
    ]
    
    # Validate payer balances
    assert payer_balances['DANNON'] == 0
    assert payer_balances['UNILEVER'] == 1500
