import json
from app import create_app, payer_balances

app = create_app()

def test_balance():
    """
    Tests the balance endpoint of the points API.

    Initializes the payer_balances dictionary with a set of test balances, then sends a GET request to the balance endpoint.
    Checks that the response status code is 200 and that the response body matches the expected payer balances.
    If the test fails, raises an AssertionError.

    Expects the following inputs:
    - None

    Returns:
    - None

    Raises:
    - AssertionError: If the test fails.
    """
    client = app.test_client()
    
    payer_balances.update({'DANNON': 1000, 'UNILEVER': 0, 'MILLER COORS': 5300})
    
    response = client.get('/balance')
    
    # Validate the response
    assert json.loads(response.data) == {'DANNON': 1000, 'UNILEVER': 0, 'MILLER COORS': 5300}
