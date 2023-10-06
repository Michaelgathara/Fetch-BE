# Fetch-BE
This project is a simple API for managing user points. Users can earn points from different payers and spend them. All transactions are recorded and sorted based on their timestamp. The system ensures that no payer's points go negative during the spending process.

## Features
* Add points to user account from different payers.
* Spend points from the user account.
* Retrieve the balance points from different payers.

## Technologies Used
* Python 3.10
* Flask
* Unittest for testing

## Project Structure
- app/: Contains the main Flask application and routes.
    - __init__.py: Flask application creation and blueprint registration.
    - routes/: Flask routes to handle API requests.
    - models.py: Data models.
    - utils/: Contains utility functions like spend.py.
    - testing/: Contains unittest test files.
        - test_add.py: Tests for adding points.
        - test_spend.py: Tests for spending points.
        - test_balance.py: Tests for balance retrieval.

## Installation
### Pre-Reqs
Acquire python from [here](https://python.org)
Acquire git from [here](https://git-scm.com/downloads)

Clone the Repository
```bash
git clone https://github.com/Michaelgathara/Fetch-BE.git
cd fetch-be            
```

### Install Required Packages
```bash
pip install -r requirements.txt
```

### Running the Application
To run the application, execute:
```bash 
python run.py
```
The API will be available at http://localhost:8000.

### Running Tests
To run all tests, execute:

```bash
python -m unittest discover -v
```
or you can execute 
```bash
python3 tester.py
```

## API Usage
#### Add Points
Endpoint: /add
Method: POST

Request Body:
```json
{
  "payer": "DANNON",
  "points": 1000,
  "timestamp": "2022-10-31T15:00:00Z"
}
```

#### Spend Points
Endpoint: /spend
Method: POST

Request Body:

```json
{
  "points": 5000
}
```

#### Get Balances
Endpoint: /balance
Method: GET
```sh
http://localhost:8000/balance
```