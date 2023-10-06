import unittest

# Import test modules
from testing.add_test import test_add
from testing.spend_test import test_spend
from testing.balance_test import test_balance

def run_all_tests():
    # Initialize the test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add tests to the test suite
    suite.addTests([
        loader.loadTestsFromModule(test_add),
        loader.loadTestsFromModule(test_spend),
        loader.loadTestsFromModule(test_balance)
    ])
    
    # Initialize a runner, pass it the suite and run it
    runner = unittest.TextTestRunner(verbosity=3)
    runner.run(suite)

if __name__ == '__main__':
    run_all_tests()
