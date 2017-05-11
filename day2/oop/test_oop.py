import unittest
from oop import BankAccount


class BankAccountTest(unittest.TestCase):
    """docstring for carClassTest"""

    def test_bankAccount_instance(self):
        bank_account = BankAccount()
        self.assertIsInstance(bank_account, BankAccount, msg='The object should be an instance of the `BankAccount` class')

    def test_object_type(self):
        bank_account = BankAccount()
        self.assertTrue((type(bank_account) is BankAccount), msg='The object should be a type of `BankAccount`')

if __name__ == '__main__':
    unittest.main()
