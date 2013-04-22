# bank account unit tests

from bankaccount import *
import unittest

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.ba1 = BankAccount("C01", 0)
    
    def test_deposit(self):  
        self.assertEqual(self.ba1.deposit(500), 200)

    def test_withdrawal(self):
        self.assertEqual(self.ba1.withdrawal(300), -300)

    def tearDown(self):
        self.ba1 = None   

# main
if __name__ == "__main__":
    unittest.main(exit=False)

    
