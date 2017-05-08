""" Demonstrates virtual wallet """


class Wallet(object):
    """ Defines blue print for digital wallet """
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        """ Adds money to wallet """
        try:
            self.balance += amount
            return self.balance
        except ValueError:
            return 'amount must be number!'

        if isinstance(amount, int):
            return 'Numbers only please!!'

    def withdraw(self):
        """ Withdraws money from wallet """