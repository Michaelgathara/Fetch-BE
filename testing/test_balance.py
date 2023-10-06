import json
from app import create_app, payer_balances

app = create_app()

def test_balance():
    """
    TODO: 
    """
    client = app.test_client()
    
    payer_balances.update({'DANNON': 1000, 'UNILEVER': 0, 'MILLER COORS': 5300})
    
    response = client.get('/balance')
    
    # Validate the response
    assert json.loads(response.data) == {'DANNON': 1000, 'UNILEVER': 0, 'MILLER COORS': 5300}
