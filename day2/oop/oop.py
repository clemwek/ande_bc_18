"""
this ia a sample use of OOP
"""

class BankAccount (object):

	def __init__(self):
		pass

	def withdraw (self):
		'''This is blank'''
		pass

	def deposit (self):
		'''this is a blank'''
		pass


class SavingsAccount (BankAccount):

	def __init__ (self):
		self.balance = 500

	def deposit (self, amount):
		if amount < 0:
			raise RuntimeError('Invalid deposit amount.')
		else :
			self.balance += amount
			return balance

	def withdraw (self, amount):
		if amount < 0:
			raise RuntimeError('Invalid deposit amount.')
		else :
			if amount > self.balance :
				raise RuntimeError('Cannot withdraw beyond the current account balance.')
			elif (self.balance-amount) < 500 :
				raise RuntimeError('Cannot withdraw beyond the minimum account balance.')
			else :
				balance = self.balance - amount
		return balance


class CurrentAccount (BankAccount):

	def __init__ (self):
		self.balance = 0

	def deposit (self, amount):
		if amount < 0:
			raise RuntimeError('Invalid deposit amount.')
		else :
			self.balance += amount
		return balance

	def withdraw (self, amount):
		if amount < 0:
			raise RuntimeError('Invalid deposit amount.')
		else :
			if amount > self.balance :
				raise RuntimeError('Cannot withdraw beyond the current account balance.')
			else :
				balance = self.balance - amount
		return balance
