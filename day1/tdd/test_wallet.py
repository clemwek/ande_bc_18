""" Tests our wallet """

import unittest
from wallet import Wallet


class TestWallet(unittest.TestCase):
    """ Tests Wallet functionality """

    def setUp(self):
        """ Gives all test cases access to an instance of the Wallet """
        self.wallet = Wallet()

    def test_deposit_works(self):
        """ Checks that deposit adds money to wallet """