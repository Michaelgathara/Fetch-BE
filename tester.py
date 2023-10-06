import unittest

# Import test scenario functions
from testing.test_add import test_add
from testing.test_spend import test_spend
from testing.test_balance import test_balance

class TestPointsManagementAPI(unittest.TestCase):
    def test_spend_points(self):
        test_spend()
    
    def test_add_points(self):
        test_add()
        
    def test_get_balance(self):
        test_balance()

if __name__ == '__main__':
    unittest.main(verbosity=3)
