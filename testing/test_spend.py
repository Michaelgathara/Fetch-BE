import json
from app import create_app, transactions, payer_balances
from app.utils import spend

app = create_app()

def test_spend():
    """
    Tests the spend endpoint of the points API.

    Initializes the transactions and payer_balances dictionaries with a set of test data, then sends a POST request to the spend endpoint with a test payload.
    Checks that the response status code is 200 and that the response body matches the expected spent points and updated payer balances.
    If any of the tests fail, raises an AssertionError.

    Expects the following inputs:
    - None

    Returns:
    - None

    Raises:
    - AssertionError: If any of the tests fail.
    """
    
    client = app.test_client()
    
    # Prepare the initial transactions and payer balances
    transactions.extend([
        { "payer": "DANNON", "points": 300, "timestamp": "2022-10-31T10:00:00Z" },
        { "payer": "UNILEVER", "points": 200, "timestamp": "2022-10-31T11:00:00Z" },
        { "payer": "DANNON", "points": -200, "timestamp": "2022-10-31T15:00:00Z" },
        { "payer": "MILLER COORS", "points": 10000, "timestamp": "2022-11-01T14:00:00Z" },
        { "payer": "DANNON", "points": 1000, "timestamp": "2022-11-02T14:00:00Z" }
    ])

    payer_balances.update({'DANNON': 1100, 'UNILEVER': 200, 'MILLER COORS': 10000})
    
    test_data = {
        'points': 5000
    }
    
    response = client.post('/spend',
                           data=json.dumps(test_data),
                           content_type='application/json')
    
    
    assert response.status_code == 200
    
    assert json.loads(response.data) == [
        {'payer': 'DANNON', 'points': -100},
        {'payer': 'UNILEVER', 'points': -200},
        {'payer': 'MILLER COORS', 'points': -4700}
    ]
    
    assert payer_balances['DANNON'] == 1000
    assert payer_balances['UNILEVER'] == 0
    assert payer_balances['MILLER COORS'] == 5300

