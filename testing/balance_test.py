import json
from app import create_app, transactions, payer_balances

app = create_app()

def test_balance():
    # Create a test client
    client = app.test_client()
    
    # Prepare the initial payer balances
    payer_balances.update({'DANNON': 1000, 'UNILEVER': 2000})
    
    # Send GET request to /balance endpoint
    response = client.get('/balance')
    
    # Validate the response
    assert response.status_code == 200
    assert json.loads(response.data) == {'DANNON': 1000, 'UNILEVER': 2000}
