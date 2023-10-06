import json
from app import create_app, transactions, payer_balances

app = create_app()

def test_add():
    # Create a test client
    client = app.test_client()
    
    # Prepare the test data
    test_data = {
        'payer': 'DANNON',
        'points': 1000,
        'timestamp': '2022-01-01T12:00:00Z'
    }
    
    # Clear existing transactions and payer balances
    transactions.clear()
    payer_balances.clear()
    
    # Send POST request to /add endpoint
    response = client.post('/add',
                           data=json.dumps(test_data),
                           content_type='application/json')
    
    # Validate the response
    assert response.status_code == 200
    
    # Validate transactions and payer balances
    assert transactions[0]['payer'] == 'DANNON'
    assert transactions[0]['points'] == 1000
    assert transactions[0]['timestamp'] == '2022-01-01T12:00:00Z'
    
    assert payer_balances['DANNON'] == 1000
